import random
from Colors import colors


class Figure:
    figures = [         # list tipov in rotacij figur
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 6, 7], [2, 6, 5, 9]],
        [[1, 2, 4, 5], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 6, 5, 9], [4, 5, 6, 9], [1, 5, 4, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):  # figuri doloci atribute
        self.x = x
        self.y = y
        self.next_type = random.randint(0, len(self.figures) - 1)
        self.type = random.randint(0, len(self.figures) - 1)
        self.next_color = random.randint(1, len(colors)-1)
        self.color = random.randint(1, len(colors)-1)
        self.rotation = 0
        self.rotated = False
        # vrne tip figure iz lista figures

    def rotate_clockwise(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])      # vrne naslednjo rotacijo figure

    def rotate_counterclockwise(self):
        if self.rotation == 0:
            self.rotation = len(self.figures[self.type]) - 1
        else:
            self.rotation = (self.rotation - 1) % len(self.figures[self.type])
