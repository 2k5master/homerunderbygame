import pygame
import os
from time import sleep
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 800
FPS = 60
VEL = 5
TIME = 60
PITCH_VEL = 7
NUM_PITCHES = 25
global bat_animation
HR = 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MLB Home Run Derby 23")



BAT_HIT = pygame.USEREVENT + 1
SWING = pygame.USEREVENT + 2

HRCOUNT_FONT = pygame.font.SysFont('comicsans', 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

homeRunBorder = pygame.image.load(
    os.path.join('assets', 'home_run_line.png'))
background = pygame.image.load(
    os.path.join('assets', 'baseball_diamond.png'))
player1 = pygame.image.load(
    os.path.join('assets', 'characterBlue (1).png'))
player1a = pygame.transform.rotate(pygame.transform.scale(player1, (20, 20)), 0)
player2 = pygame.image.load(
    os.path.join('assets', 'characterBlue (4).png'))
player2a = pygame.transform.rotate(player2, 270)
baseball_bat = pygame.image.load(
    os.path.join('assets', 'bat.png'))
baseball_bat1 = pygame.transform.rotate(baseball_bat, 225)
baseball = pygame.image.load(
    os.path.join('assets', 'ball.png'))
bat_anim_default = pygame.image.load(
    os.path.join('assets', 'bat.png'))
bat_anim = pygame.transform.rotate(baseball_bat, 270)



def player_handle_movement(keys_pressed, red):
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # UP
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]: # DOWN
            red.y += VEL
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0: # LEFT
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: # RIGHT
            red.x += VEL


def handle_pitches(bat, pitches):
    for pitch in pitches:
        pitch.y += PITCH_VEL
        if bat.colliderect(pitch):
            pygame.event.post(pygame.event.Event(BAT_HIT))
        elif pitch.y > WIDTH:
            pitches.remove(pitch)

                




def draw_window(red, pitcher, bat, pitches, swings, bat_animation):
    WIN.fill(WHITE)
    WIN.blit(background, (0, 0))
    hr_count_text = HRCOUNT_FONT.render("Home Runs: " + str(HR), 1, BLACK)
    WIN.blit(hr_count_text, (WIDTH - hr_count_text.get_width() - 10, 10))
    WIN.blit(homeRunBorder, (0, -120))
    WIN.blit(player1a, (red.x, red.y))
    WIN.blit(player2a, (pitcher.x, pitcher.y))
    for pitch in pitches:
        pygame.draw.rect(WIN, BLACK, pitch)
    if bat_animation == False:
        WIN.blit(baseball_bat1, (bat.x, bat.y))
    elif bat_animation == True:
        for bat in swings:
            WIN.blit(bat_anim, (bat.x, bat.y))
        bat_animation = False
    pygame.display.update()

        

def main():
    red = pygame.Rect(410, 675, WIDTH, HEIGHT)
    pitcher = pygame.Rect(438, 480, WIDTH, HEIGHT)
    bat = pygame.Rect(420, 687, WIDTH, HEIGHT)
    bat_animation = False
    pitches = []
    swings = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and len(pitches) < NUM_PITCHES:
                    pitch = pygame.Rect(pitcher.x, pitcher.y, 10, 5)
                    pitches.append(pitch)
                if event.key == pygame.K_SPACE:
                    swings.append(bat)
                    bat_animation = True



            
        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, red)
        handle_pitches(bat, pitches)
        draw_window(red, pitcher, bat, pitches, swings, bat_animation)


    pygame.quit()

if __name__ == "__main__":
    main()