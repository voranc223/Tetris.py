from Colors import *
from field_creation import *
pygame.init()


size = (600, 600)
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
done = False
clock = pygame.time.Clock()
števec=0
a_pressed = False
d_pressed = False


while not done:  #glavna zanka
    if game.figure == None:               # kliče funkcijo (nova_figura)
        game.nova_figura()
    if game.lines % 10 == 0:
        game.level = 1+game.lines // 10
    števec += 1
    if števec > 100000:
        števec = 0
    if števec % (fps // 3 - game.level*2) == 0:
        if game.state == "start":
            game.pojdi_dol()
    for event in pygame.event.get():      #izhod iz okna
        if event.type == pygame.QUIT:
            done = True
        if game.state == "start":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.pojdi_dol()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    a_pressed = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    d_pressed = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.rotiraj_se()
                if event.key == pygame.K_SPACE:
                    game.pojdi_do_dna()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20,10)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    a_pressed = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    d_pressed = False
    if števec % 5 == 0:    #dovoli držanje tipke za hitrejše premikanje
        if a_pressed:
            game.pojdi_v_stran(-1)
        if d_pressed:
            game.pojdi_v_stran(1)

    screen.fill(blue)
    pygame.draw.rect(screen, (red), [game.x-3, game.y-3, game.zoom * game.width+6, game.zoom * game.height+6], 3)
    pygame.draw.rect(screen, (dark_purple), [game.x, game.y, game.zoom * game.width, game.zoom * game.height])

    for i in range(game.height):          # nariše polje
        for j in range(game.width):
            pygame.draw.rect(screen, dark_blue, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom],1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 2])

    if game.figure is not None:           # nariše figuro
        for i in range(4):
            for y in range(4):
                a=i*4+y
                if a in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],[game.x + game.zoom*(y + game.figure.x)+1,
                                                                 game.y + game.zoom * (i+game.figure.y)+1,
                                                                 game.zoom-2, game.zoom-2])
    font = pygame.font.SysFont('Calibri', 40, True, False)
    font1 = pygame.font.SysFont('Calibri', 80, True, False)
    score_surface = font.render("Score:", True, WHITE)
    level_surface = font.render("Level:", True, WHITE)
    score_rect = pygame.Rect(15, 55, 150, 60)
    level_rect = pygame.Rect(440, 55, 150, 60)
    score_value_surface = font.render(str(game.score), True, WHITE)
    level_value_surface = font.render(str(game.level), True, WHITE)
    Tetris1_Caption = font1.render("TETRIS", True, WHITE)
    screen.blit(score_surface, (40, 20, 50, 50))
    screen.blit(level_surface, (470, 20, 50, 50))
    pygame.draw.rect(screen, ((59, 85, 162)), score_rect, 0, 10)
    pygame.draw.rect(screen, ((59, 85, 162)), level_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                  centery=score_rect.centery))
    screen.blit(level_value_surface, level_value_surface.get_rect(centerx=level_rect.centerx,
                                                                  centery=level_rect.centery))
    screen.blit(Tetris1_Caption, (200, 20, 50, 50))
    if game.state == "gameover":
        screen.blit(font1.render("Game Over", True, ((255, 0, 0))), [125, 200])
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
