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
beats = 8
instruments = 6

# for i in range(instruments):
#     spacing = (i * 100) + 34

def draw_grid():
    left_menu = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 198], 2)
    lower_menu = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 2)
    pads = []
    colors = [gray, white, gray]
    kick_text = label_font.render("Kick", True, white)
    sub_text = label_font.render("808", True, white)
    snare_text = label_font.render("Snare", True, white)
    clap_text = label_font.render("Clap", True, white)
    hi_hat_text = label_font.render("Hi-hat", True, white)
    crash_text = label_font.render("Crash", True, white)

    screen.blit(kick_text, (52, 34))
    screen.blit(sub_text, (52, 134))
    screen.blit(snare_text, (52, 234))
    screen.blit(clap_text, (52, 334))
    screen.blit(hi_hat_text, (52, 434))
    screen.blit(crash_text, (52, 534))

    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (198, (i * 100) + 100), 2)

    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gray, [i * ((WIDTH - 198) // beats) + 198, (j * 100),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 1, 2)

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
