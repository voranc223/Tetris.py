import pygame
from object_creation import Figure


pygame.init()

class Tetris:
    def __init__(self, height, width):
        self.state = "start"
        self.x = 175
        self.y = 98
        self.zoom = 25
        self.height = height
        self.width = width
        self.figure = None
        self.field=[]
        self.state = "start"
        self.score = 0
        self.lines = 0
        self.level = 1
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        pygame.mixer.music.load("Sounds/Tetris.theme.sound.mp3")
        pygame.mixer.music.play(-1)
        for i in range(self.height):
            nova_linija = []
            for y in range(self.width):
                nova_linija.append(0)
            self.field.append(nova_linija)
    def nova_figura(self):      #ustvari figuro in ji določi začetne koordinate
        self.figure = Figure(3, 0)
    def intersekcija(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                a = i * 4 + j
                if a in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or\
                            j + self.figure.x < 0 or\
                            self.field[i + game.figure.y][j+game.figure.x] > 0:
                                intersection = True
        return intersection
    def uniči_polne_vrste(self):
        for i in range(1, self.height):
            a = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    a = a+1
            if a == 0:
                self.clear_sound.play()
                self.lines += 1
                self.score += 40*self.level
                for b in range(i, 1, -1):
                    for j in range(game.width):
                        self.field[b][j] = self.field[b-1][j]

    def zamrzni(self):
        for i in range(4):
            for y in range(4):
                a = i * 4 + y
                if a in self.figure.image():
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
    def pojdi_v_stran(self,x):
        self.figure.x += x
        if self.intersekcija():
            self.figure.x -= x
    def rotiraj_se(self):
        last_rotation = self.figure.rotation
        self.figure.rotate()
        pygame.mixer.Sound.play(self.rotate_sound)
        if self.intersekcija():
            self.figure.rotation = last_rotation
    def pojdi_do_dna(self):
        while not self.intersekcija():
            self.figure.y += 1
        self.figure.y -= 1
        self.zamrzni()
game = Tetris(20, 10)
