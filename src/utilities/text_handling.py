# Created by a human
# when:
# 10/26/2015
# 4:09 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame

#these are just two methods that do the same thing with different arguments
def print_info(surface, msg, x, row=0):
    font = pygame.font.Font(None, 12)
    text = font.render(msg, 1, (254,254,254))
    pos = [x,10+16*row]
    surface.blit(text, pos)
# they are used to put text on a surface, message = 'whatever you want'
def display_info(surface, message, font_size,  x, y):
    near_white = (254,254,254)
    font = pygame.font.Font(None, font_size)
    text = font.render(message, 1, near_white)
    pos = [x,y]
    surface.blit(text, pos)

def text_widget(r,g,b, text, size, x,y):
    screen = pygame.display.get_surface()
    col = pygame.Color((r,g,b))