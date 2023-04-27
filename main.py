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

run = True

while run:
    TIMER.tick(FPS)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
