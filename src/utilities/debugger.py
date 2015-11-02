# Created by a human
# when:
# 11/1/2015
# 2:54 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame

def screen_print(surf, msg, x=10,row=0):
    font = pygame.font.Font(None, 16)
    text = font.render(msg, 1, (254,254,254))
    pos = [x,10+16*row]
    surf.blit(text, pos)

def display_mouse_info():
    screen = pygame.display.get_surface()
    mos_pos = pygame.mouse.get_pos()
    screen_print(screen, str(mos_pos))

def display_pygame_event_info():
    screen = pygame.display.get_surface()
    screen_print(screen, str(pygame.event.get()))