import pygame
from pygame import mixer

pygame.init()

# Screen
WIDTH = 1400
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('TR-808')
label_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 24)

# Colors
black = (0, 0, 0)
white =(255, 255, 255)
gray =(128, 128, 128)
light_gray = (170, 170, 170)
dark_gray = (50, 50, 50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

# Starting variables
FPS = 60
TIMER = pygame.time.Clock()
index = 100
beats = 8
instruments = 6
pads = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_channels = [1 for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 0
beat_changed = True
save_menu = False
load_menu = False
saved_beats = []
file = open('saved_beats.txt', 'r')
for line in file:
    saved_beats.append(line)

beat_name = ''
typing = False

# sounds
kick =mixer.Sound('media/TR-808 sounds/Kick.wav')
sub =mixer.Sound('media/TR-808 sounds/808 Sub.wav')
snare =mixer.Sound('media/TR-808 sounds/Snare 1.wav')
clap =mixer.Sound('media/TR-808 sounds/Clap 1.wav')
hi_hat =mixer.Sound('media/TR-808 sounds/Closed Hat 1.wav')
crash =mixer.Sound('media/TR-808 sounds/Cymbal.wav')
pygame.mixer.set_num_channels(instruments * 3)


def play_notes():
    for pad in range(len(clicked)):
        if clicked[pad][active_beat] == 1 and active_channels[pad] == 1:
            if pad == 0:
                kick.play()
            if pad == 1:
                sub.play()
            if pad == 2:
                snare.play()
            if pad == 3:
                clap.play()
            if pad == 4:
                hi_hat.play()
            if pad == 5:
                crash.play()


def draw_grid(clicks, active_beat, active_channels):
    left_menu = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 198], 2)
    lower_menu = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 2)
    pads = []
    colors = [gray, white, gray]
    kick_text = label_font.render("Kick", True, colors[active_channels[0]])
    sub_text = label_font.render("808", True, colors[active_channels[1]])
    snare_text = label_font.render("Snare", True, colors[active_channels[2]])
    clap_text = label_font.render("Clap", True, colors[active_channels[3]])
    hi_hat_text = label_font.render("Hi-hat", True, colors[active_channels[4]])
    crash_text = label_font.render("Crash", True, colors[active_channels[5]])

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
                if active_channels[inst] == 1:
                    color = green
                else:
                    color = dark_gray

            rect = pygame.draw.rect(screen, color, [beat * ((WIDTH - 198) // beats) + 198, ((inst * 100)),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 0, 2)

            rect = pygame.draw.rect(screen, gold, [beat * ((WIDTH - 198) // beats) + 198, ((inst * 100) + 1),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 2, 2)

            rect = pygame.draw.rect(screen, black, [beat * ((WIDTH - 198) // beats) + 198, ((inst * 100) + 1),
                                     ((WIDTH - 198) // beats), ((HEIGHT - 198) // instruments)], 1, 2)

            pads.append((rect, (beat, inst)))

        active = pygame.draw.rect(screen, blue, [active_beat * ((WIDTH - 200)// beats) + 198, 0, ((WIDTH - 200)// beats), instruments * 100], 2, 3)
    return pads


def draw_save_menu(beat_name, typing):
    pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT])
    menu_text = label_font.render('Save Menu: Enter a name', True, white)
    screen.blit(menu_text, (485, 40))
    saving_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 100, HEIGHT * 0.75, 200, 100], 0, 5)
    save_txt = label_font.render('Save Beat', True, white)
    screen.blit(save_txt, (WIDTH // 2 - 80, HEIGHT * 0.75 + 35))
    if typing:
        pygame.draw.rect(screen, dark_gray, (400, 200,600,200), 0, 5)

    entry_rect = pygame.draw.rect(screen, gray, (400, 200,600,200), 2, 5)
    entry_text = label_font.render(f'{beat_name}', True, white)
    screen.blit(entry_text, (430, 250))

    exit_btn = pygame.draw.rect(screen, gray, [1280, HEIGHT - 140, 100, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (1285, HEIGHT - 110))

    return exit_btn, saving_btn, entry_rect


def draw_load_menu(index):
    loaded_clicked = 0
    loaded_beats = 0
    loaded_bpm = 0
    pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT])
    menu_text = label_font.render('Load Menu: Choose a beat', True, white)
    screen.blit(menu_text, (485, 40))
    loading_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 + 25, HEIGHT * 0.75, 200, 100], 0, 5)
    load_txt = label_font.render('Load Beat', True, white)
    screen.blit(load_txt, (WIDTH // 2 + 47, HEIGHT * 0.75 + 35))
    delete_btn = pygame.draw.rect(screen, gray, [(WIDTH // 2) - 225, HEIGHT * 0.75, 200, 100], 0, 5)
    delete_text = label_font.render('Delete Beat', True, white)
    screen.blit(delete_text, ((WIDTH // 2) - 215, HEIGHT * 0.75 + 35))
    exit_btn = pygame.draw.rect(screen, gray, [1280, HEIGHT - 140, 100, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (1285, HEIGHT - 110))

    pygame.draw.rect(screen, gray, (190, 90, 1000, 500), 2, 3)
    loaded_rect = pygame.draw.rect(screen, gray, [190, 90, 1000, 500], 2, 5)
    if 0 <= index < len(saved_beats):
        pygame.draw.rect(screen, light_gray, [190, 100 + index * 50, 1000, 50])

    for beat in range(len(saved_beats)):
        if beat < 10:
            beat_clicked = []
            row_text = medium_font.render(f'{beat + 1}', True, white)
            screen.blit(row_text, (200, 100 + beat * 50))
            name_index_start = saved_beats[beat].index('name: ') + 6
            name_index_end = saved_beats[beat].index(', beats:')
            name_text = medium_font.render(saved_beats[beat][name_index_start:name_index_end], True, white)
            screen.blit(name_text, (240, 100 + beat * 50))
        if 0 <= index < len(saved_beats) and beat == index:
            beat_index_end = saved_beats[beat].index(', bpm:')
            loaded_beats = int(saved_beats[beat][name_index_end + 8: beat_index_end])
            bpm_index_end = saved_beats[beat].index(', selected:')
            loaded_bpm = int(saved_beats[beat][beat_index_end + 6: bpm_index_end])
            loaded_clicks_string = saved_beats[beat][bpm_index_end + 14: -3]
            loaded_clicks_rows = list(loaded_clicks_string.split('], ['))
            for row in range(len(loaded_clicks_rows)):
                loaded_clicks_row = (loaded_clicks_rows[row].split(', '))
                for item in range(len(loaded_clicks_row)):
                    if loaded_clicks_row[item] == '1' or loaded_clicks_row[item] == '-1':
                        loaded_clicks_row[item] = int(loaded_clicks_row[item])
                beat_clicked.append(loaded_clicks_row)
                loaded_clicked = beat_clicked
    loaded_info = [loaded_beats, loaded_bpm, loaded_clicked]


    return exit_btn, loading_btn, delete_btn, loaded_rect, loaded_info

run = True
while run:
    TIMER.tick(FPS)
    screen.fill(black)

    pads = draw_grid(clicked, active_beat, active_channels)

    # lower menu
    # play pause button
    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 200, 100], 0, 5)

    if playing:
        play_text = label_font.render('Pause', True, dark_gray)
        screen.blit(play_text, (100, HEIGHT - 115))
    else:
        play_text = label_font.render('Play', True, dark_gray)
        screen.blit(play_text, (111, HEIGHT - 115))

    # bpm buttons
    bpm_rect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 200, 100], 2, 5)
    bpm_text = label_font.render('BPM', True, white)
    screen.blit(bpm_text, ( 360, HEIGHT - 136))
    bpm_text2 = label_font.render(f'{bpm // 2}', True, white)
    screen.blit(bpm_text2, ( 367, HEIGHT - 96))

    bpm_add_rect1 = pygame.draw.rect(screen, gray, [510, HEIGHT - 150, 48, 48], 0, 5)
    bpm_sub_rect1 = pygame.draw.rect(screen, gray, [510, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render('+1', True, white)
    sub_text = medium_font.render('-1', True, white)
    screen.blit(add_text, (520, HEIGHT - 140))
    screen.blit(sub_text, (520, HEIGHT - 90))

    bpm_add_rect5 = pygame.draw.rect(screen, gray, [560, HEIGHT - 150, 48, 48], 0, 5)
    bpm_sub_rect5 = pygame.draw.rect(screen, gray, [560, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render('+5', True, white)
    sub_text = medium_font.render('-5', True, white)
    screen.blit(add_text, (570, HEIGHT - 140))
    screen.blit(sub_text, (570, HEIGHT - 90))
    # Time Signature
    timesig_rect = pygame.draw.rect(screen, gray, [650, HEIGHT - 150, 200, 100], 2, 5)
    timesig_text = label_font.render('Time Sig.', True, white)
    screen.blit(timesig_text, ( 678, HEIGHT - 136))
    timesig_text2 = label_font.render(f'{beats}', True, white)
    screen.blit(timesig_text2, ( 740, HEIGHT - 96))

    timesig_add_rect1 = pygame.draw.rect(screen, gray, [860, HEIGHT - 150, 48, 48], 0, 5)
    timesig_sub_rect1 = pygame.draw.rect(screen, gray, [860, HEIGHT - 100, 48, 48], 0, 5)
    timesig_add_text = medium_font.render('+1', True, white)
    timesig_sub_text = medium_font.render('-1', True, white)
    screen.blit(timesig_add_text, (870, HEIGHT - 140))
    screen.blit(timesig_sub_text, (870, HEIGHT - 90))

    # instrument toggle
    instrument_rects = []
    for inst in range(instruments):
        rect = pygame.rect.Rect((0, inst * 100), (198, 100))
        instrument_rects.append(rect)

    # Save and load patterns
    save_button = pygame.draw.rect(screen, gray, [950, HEIGHT - 150, 120, 48], 0, 5)
    load_button = pygame.draw.rect(screen, gray, [950, HEIGHT - 100, 120, 48], 0, 5)
    save_text = label_font.render('Save', True, white)
    load_text = label_font.render('Load', True, white)
    screen.blit(save_text, (970, HEIGHT - 140))
    screen.blit(load_text, (970, HEIGHT - 90))

    # clear pads
    clear_pads = pygame.draw.rect(screen, gray, [1110, HEIGHT - 100, 120, 48], 0, 5)
    clear_text = label_font.render('Clear', True, white)
    screen.blit(clear_text, (1125, HEIGHT - 90))

    if beat_changed:
        play_notes()
        beat_changed = False

    if save_menu:
        exit_button, saving_btn, entry_rect = draw_save_menu(beat_name, typing)
        playing = False
    if load_menu:
        exit_button, load_button, delete_btn, loaded_rect, loaded_info = draw_load_menu(index)
        playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu:
            for pad in range(len(pads)):
                if pads[pad][0].collidepoint(event.pos):
                    coords = pads[pad][1]
                    clicked[coords[1]][coords[0]] *= -1

        if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True

            if bpm_add_rect1.collidepoint(event.pos):
                bpm += 2
            elif bpm_sub_rect1.collidepoint(event.pos):
                bpm -= 2
            elif bpm_add_rect5.collidepoint(event.pos):
                bpm += 10
            elif bpm_sub_rect5.collidepoint(event.pos):
                bpm -= 10
            elif timesig_add_rect1.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif timesig_sub_rect1.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            elif clear_pads.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

            elif save_button.collidepoint(event.pos):
                save_menu = True
            elif load_button.collidepoint(event.pos):
                load_menu = True

            for inst in range(len(instrument_rects)):
                if instrument_rects[inst].collidepoint(event.pos):
                    active_channels[inst] *= -1

        elif event.type == pygame.MOUSEBUTTONUP:
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                playing = True
                beat_name = ''
                typing = False
            if load_menu:
                if loaded_rect.collidepoint(event.pos):
                    index = (event.pos[1] - 100) // 50
                elif delete_btn.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        saved_beats.pop(index)
                elif load_button.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        beats = loaded_info[0]
                        bpm = loaded_info[1]
                        clicked = loaded_info[2]
                        index = 100
                        load_menu = False
                        playing = True
                        active_beat = -1

            if save_menu:
                if entry_rect.collidepoint(event.pos):
                    if typing:
                        typing = False
                    elif not typing:
                        typing = True
                if saving_btn.collidepoint(event.pos):
                    file = open('saved_beats.txt', 'w')
                    saved_beats.append(f'\nname: {beat_name}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                    for beat in range(len(saved_beats)):
                        file.write(str(saved_beats[beat]))
                    file.close()
                    save_menu = False
                    typing = False
                    beat_name = ''

        if event.type == pygame.TEXTINPUT and typing:
            beat_name += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beat_name) > 0 and typing:
                beat_name = beat_name[: -1]

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
