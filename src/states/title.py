# Created by a human
# when:
# 10/27/2015
# 9:29 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from game import Game
from ..utilities import image_handling
import pygame


class Title(State):
    def __init__(self):
        State.__init__(self)
        self.canvas = image_handling.get_image('img/titlescreen/title.png')
        self.next_state = Game()
        self.canvas = pygame.transform.scale(self.canvas, self.screen.get_size())
        self.img_pos = image_handling.center(self.canvas.get_size(), self.screen.get_size())



    def check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.VIDEORESIZE:
                self.canvas = pygame.transform.scale(self.canvas, (e.w, e.h))
                self.screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            if e.type == pygame.QUIT:
                self.close_game()


    def update_screen(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.canvas, self.img_pos)
        pygame.display.update()

    def quit(self):
        State.quit(self)