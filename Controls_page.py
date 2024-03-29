import pygame
from Colors import *
pygame.init()

font = pygame.font.SysFont('Calibri', 40, True, False)
font1 = pygame.font.SysFont('Calibri', 80, True, False)
small_font = pygame.font.SysFont('Tahoma', 20, True, False)
size = (600, 600)
screen = pygame.display.set_mode(size)
Continue_Caption = font.render("PRESS C TO CONTINUE", True, red)
Controls_Caption = font1.render("Controls", True, red)
escape_Caption = small_font.render("press esc to restart", True, orange)
Space_Caption = small_font.render("press space to hard drop", True, orange)
Arrow_controls = pygame.image.load("images/tetris-controls.png")
Or_caption = font.render("or", True, orange)



def image_scailing(image, size):
    image = pygame.transform.scale(image, size)
    return image
space_key_image = image_scailing(pygame.image.load("images/space_bar_image.png"), (200, 130))
esc_key_image = image_scailing(pygame.image.load("images/escape_key_image.png"), (200, 130))
awsd_keys_image = image_scailing(pygame.image.load("images/awsd_keys.jpg"), (200, 130))
def controls_page():
    screen.fill(WHITE)
    screen.blit(Controls_Caption, (170, 0))
    screen.blit(Continue_Caption, (120, 550))
    screen.blit(Arrow_controls, (20, 70))
    screen.blit(space_key_image, (20, 260))
    screen.blit(esc_key_image, (20, 400))
    screen.blit(escape_Caption, (230, 460))
    screen.blit(Space_Caption, (260, 300))
    screen.blit(awsd_keys_image, (350, 90))
    screen.blit(Or_caption, (250, 120))
