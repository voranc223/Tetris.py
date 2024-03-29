import pygame.mixer
from Controls_page import controls_page, Continue_Caption
from Colors import *
from field_creation import *
import Button
pygame.init()


size = (600, 600)
screen = pygame.display.set_mode(size)
fps = 60
pygame.display.set_caption("Tetris")
done = False
clock = pygame.time.Clock()
counter = 0
a_pressed = False
d_pressed = False
font = pygame.font.SysFont('Calibri', 40, True, False)
font1 = pygame.font.SysFont('Calibri', 80, True, False)
score_surface = font.render("Score:", True, WHITE)
level_surface = font.render("Level:", True, WHITE)
next_surface = font.render("Next:", True, WHITE)
Tetris1_Caption = font1.render("TETRIS", True, WHITE)
Settings_Caption = font1.render("Controls", True, red)
Controls_Caption = font.render("Controls", True, WHITE)
Paused_Caption = font1.render("PAUSED", True, WHITE)
score_rect = pygame.Rect(15, 55, 150, 60)
level_rect = pygame.Rect(440, 55, 150, 60)
next_rect = pygame.Rect(20, 200, 120, 120)
next_figure_offset_x = [33, 10, 30, 20, 20, 33, 20]
next_figure_offset_y = [10, 35, 35, 23, 23, 30, 33]
settings_image = pygame.image.load("images/settings_slika.png")
settings_button = Button.button(480, 400, 80, 70, settings_image, screen)
Pause_button = Button.button(20, 400, 80, 70, pygame.image.load("images/pause_button_image.png"), screen)


def paused():
    pause = True
    while pause:
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.mixer.music.play(-1)
                    pause = False
        if settings_button.clicked is True:
            controls_page()
        if Pause_button.clicked is True:
            screen.blit(Paused_Caption, (170, 200))
            screen.blit(Continue_Caption, (120, 400))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pygame.mixer.music.play(-1)
                        pause = False
        pygame.display.update()
        clock.tick(5)


while not done:  # glavna zanka
    if game.state == "pre_game":
        pygame.mixer.music.stop()
        for event in pygame.event.get():  # izhod iz okna
            if event.type == pygame.QUIT:
                done = True
        screen.fill(blue)
        start_message = font.render("Press START to start", True, BLACK)
        screen.blit(start_message, (130, 50))
        Start_button = Button.button(200, 300, 200, 150, pygame.image.load("images/Start_tetris_image.png"), screen)
        Start_button.draw()
        if Start_button.clicked is True:
            game.state = "start"
            pygame.mixer.music.play(-1)
    elif game.state == "start":
        if game.figure is None:               # kliče funkcijo (nova_figura)
            game.nova_figura()
        if game.lines % 10 == 0:
            game.level = 1 + game.lines // 10
        counter += 1
        if counter > 100000:
            counter = 0
        if counter % (fps // 3 - game.level * 2) == 0:
            if game.state == "start":
                game.pojdi_dol()
        for event in pygame.event.get():      # izhod iz okna
            if event.type == pygame.QUIT:
                done = True
            if game.state == "start":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        game.rotiraj_se(1)
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_r:
                        game.rotiraj_se(2)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        game.pojdi_dol()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        a_pressed = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        d_pressed = True
                    if event.key == pygame.K_SPACE:
                        game.pojdi_do_dna()
                    if event.key == pygame.K_ESCAPE:
                        game.__init__(20, 10)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        a_pressed = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        d_pressed = False
        if counter % 5 == 0:    # dovoli držanje tipke za hitrejše premikanje
            if a_pressed:
                game.pojdi_v_stran(-1)
            if d_pressed:
                game.pojdi_v_stran(1)
        if settings_button.clicked is True:
            paused()
        if Pause_button.clicked is True:
            paused()

        screen.fill(blue)
        settings_button.draw()
        Pause_button.draw()
        pygame.draw.rect(screen, red, [game.x-3, game.y-3, game.zoom * game.width+6, game.zoom * game.height+6], 3)
        pygame.draw.rect(screen, dark_purple, [game.x, game.y, game.zoom * game.width, game.zoom * game.height])
        pygame.draw.rect(screen, blue_1, next_rect, 0, 10)
        for i in range(game.height):          # nariše polje
            for j in range(game.width):
                pygame.draw.rect(screen, dark_blue, [game.x + game.zoom * j, game.y + game.zoom * i,
                                                     game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, colors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1,
                                      game.zoom - 1, game.zoom - 1])

        if game.figure is not None:           # nariše figuro
            for i in range(4):
                for y in range(4):
                    a = i * 4 + y
                    if a in game.image():
                        pygame.draw.rect(screen, colors[game.figure.color],
                                         [game.x + game.zoom*(y + game.figure.x)+1,
                                          game.y + game.zoom * (i+game.figure.y)+1,
                                          game.zoom-1, game.zoom-1])
        if game.figure is not None:           # nariše naslednjo figuro
            for i in range(4):
                for y in range(4):
                    a = i * 4 + y
                    if a in game.image_next():
                        pygame.draw.rect(screen, colors[game.next_figure_color],
                                         [20 + next_figure_offset_x[game.next_type_figure] + game.zoom*y,
                                          200 + next_figure_offset_y[game.next_type_figure] + game.zoom * i,
                                          game.zoom - 1, game.zoom - 1])

        score_value_surface = font.render(str(game.score), True, WHITE)
        level_value_surface = font.render(str(game.level), True, WHITE)
        screen.blit(score_surface, (40, 20, 50, 50))
        screen.blit(level_surface, (470, 20, 50, 50))
        pygame.draw.rect(screen, blue_1, score_rect, 0, 10)
        pygame.draw.rect(screen, blue_1, level_rect, 0, 10)
        next_rect.centerx = score_rect.centerx
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                      centery=score_rect.centery))
        screen.blit(level_value_surface, level_value_surface.get_rect(centerx=level_rect.centerx,
                                                                      centery=level_rect.centery))
        screen.blit(next_surface, next_surface.get_rect(centerx=score_rect.centerx, centery=next_rect.centery - 80))
        screen.blit(Controls_Caption, (450, 350))
        screen.blit(Tetris1_Caption, (200, 20, 50, 50))
    elif game.state == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)
        screen.blit(font1.render("Game Over", True, red), [125, 200])
        pygame.mixer.music.stop()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
