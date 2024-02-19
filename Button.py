import pygame

pygame.init()

class button:
    def __init__(self, x, y, button_width, button_hight, image,surface):
        self.image = pygame.transform.scale(image, (button_width, button_hight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.surface = surface
        self.clicked = False

    def draw(self):
        action = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
