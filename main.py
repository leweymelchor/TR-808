import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white =(255, 255, 255)
gray =(128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('TR-808')
label_font = pygame.font.Font('freesansbold.ttf', 32)

FPS = 60
TIMER = pygame.time.Clock()


def draw_grid():
    left_menu = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 195], 5)
    lower_menu = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    pads = []
    colors = [gray, white, gray]
    kick_text = label_font.render("Kick", True, white)
    sub_text = label_font.render("808", True, white)
    snare_text = label_font.render("Snare", True, white)
    clap_text = label_font.render("Clap", True, white)
    hi_hat_text = label_font.render("Hi-hat", True, white)
    crash_text = label_font.render("Crash", True, white)

    screen.blit(kick_text, (30, 30))
    screen.blit(sub_text, (30, 130))
    screen.blit(snare_text, (30, 230))
    screen.blit(clap_text, (30, 330))
    screen.blit(hi_hat_text, (30, 430))
    screen.blit(crash_text, (30, 530))

run = True
while run:
    TIMER.tick(FPS)
    screen.fill(black)
    draw_grid()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
