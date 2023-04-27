import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white =(255, 255, 255)
gray =(128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('TR-808')
label_font = pygame.font.Font('freesansbold.ttf', 32)

FPS = 60
TIMER = pygame.time.Clock()
beats = 8
instruments = 6
pads = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 0
beat_changed = True

# for i in range(instruments):
#     spacing = (i * 100) + 34

def draw_grid(clicks, active_beat):
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

    for inst in range(instruments):
        pygame.draw.line(screen, gray, (0, (inst * 100) + 100), (198, (inst * 100) + 100), 2)

    for beat in range(beats):
        for inst in range(instruments):
            if clicks[inst][beat] == -1:
                color = gray
            else:
                color = green

            rect = pygame.draw.rect(screen, color, [beat * ((WIDTH - 198) // beats) + 198, ((inst * 100)),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 0, 2)

            rect = pygame.draw.rect(screen, gold, [beat * ((WIDTH - 198) // beats) + 198, ((inst * 100) + 1),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 2, 2)

            rect = pygame.draw.rect(screen, black, [beat * ((WIDTH - 198) // beats) + 198, ((inst * 100) + 1),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 1, 2)

            pads.append((rect, (beat, inst)))

        active = pygame.draw.rect(screen, blue, [active_beat * ((WIDTH - 200)// beats) + 200, 0, ((WIDTH - 200)// beats), instruments * 100], 2, 3)
    return pads


run = True
while run:
    TIMER.tick(FPS)
    screen.fill(black)
    pads = draw_grid(clicked, active_beat)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for pad in range(len(pads)):
                if pads[pad][0].collidepoint(event.pos):
                    coords = pads[pad][1]
                    clicked[coords[1]][coords[0]] *= -1

    beat_length = (FPS * 60) // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()

pygame.quit()
