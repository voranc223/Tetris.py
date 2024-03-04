import pygame
import random
from object_creation import Figure
from Colors import colors


pygame.init()


class Tetris:
    def __init__(self, height, width):
        self.state = "pre_game"
        self.x = 175
        self.y = 98
        self.zoom = 25
        self.height = height
        self.width = width
        self.figure = None
        self.field = []
        self.score = 0
        self.lines = 0
        self.lines_cleared = 0
        self.level = 1
        self.next_type_figure = random.randint(0, 6)
        self.next_figure_color = random.randint(1, 6)
        self.tetris_clear_sound = pygame.mixer.Sound("Sounds/tetris-line-clear-sound.mp3")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        pygame.mixer.music.load("Sounds/Tetris.theme.sound.mp3")
        pygame.mixer.music.play(-1)
        for i in range(self.height):
            nova_linija = []
            for y in range(self.width):
                nova_linija.append(0)
            self.field.append(nova_linija)

    def nova_figura(self):      # ustvari figuro in ji določi začetne koordinate
        self.figure = Figure(3, 0)
        self.figure.type = self.next_type_figure
        self.figure.color = self.next_figure_color
        self.next_type_figure = random.randint(0, len(self.figure.figures)-1)
        self.next_figure_color = random.randint(1, len(colors)-1)

    def image(self):
        return self.figure.figures[self.figure.type][self.figure.rotation]

    def image_next(self):
        return self.figure.figures[self.next_type_figure][0]

    def intersekcija(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                a = i * 4 + j
                if a in self.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or\
                            j + self.figure.x < 0 or\
                            self.field[i + game.figure.y][j+game.figure.x] > 0:
                        intersection = True
        return intersection

    def uniči_polne_vrste(self):
        self.lines_cleared = 0
        for i in range(1, self.height):
            a = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    a = a+1
            if a == 0:
                self.lines += 1
                self.lines_cleared += 1
                for b in range(i, 1, -1):
                    for j in range(game.width):
                        self.field[b][j] = self.field[b-1][j]
        if 4 > self.lines_cleared > 0:
            self.clear_sound.play()
            if self.lines_cleared == 1:
                self.score += 100 * self.level
                if self.figure.rotated is True:
                    self.score += 100 * self.level
            elif self.lines_cleared == 2:
                self.score += 300 * self.level
                if self.figure.rotated is True:
                    self.score += 300 * self.level
            elif self.lines_cleared == 3:
                self.score += 500 * self.level
        elif self.lines_cleared == 4:
            self.tetris_clear_sound.play()
            self.score += 800 * self.level

    def zamrzni(self):
        for i in range(4):
            for y in range(4):
                a = i * 4 + y
                if a in self.image():
                    self.field[self.figure.y + i][self.figure.x + y] = self.figure.color
        self.nova_figura()
        self.uniči_polne_vrste()
        if self.intersekcija():
            self.state = "gameover"

    def pojdi_dol(self):
        self.figure.y += 1
        if self.intersekcija():
            self.figure.y -= 1
            self.zamrzni()

    def pojdi_v_stran(self, x):
        self.figure.x += x
        if self.intersekcija():
            self.figure.x -= x

    def rotiraj_se(self, rotation):
        last_rotation = self.figure.rotation
        if rotation == 1:
            self.figure.rotate_clockwise()
        else:
            self.figure.rotate_counterclockwise()
        pygame.mixer.Sound.play(self.rotate_sound)
        if self.intersekcija():
            self.figure.rotation = last_rotation

    def pojdi_do_dna(self):
        while not self.intersekcija():
            self.figure.y += 1
        self.figure.y -= 1
        self.zamrzni()


game = Tetris(20, 10)
