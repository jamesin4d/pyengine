# Created by a human
# when:
# 10/26/2015
# 1:25 PM
#
#
# --------------------------------------------------------------------
from ..eng import State
import pygame

class Game(State):

    def __init__(self):
        State.__init__(self)

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.quit()

    def check_collisions(self):
        pass

    def update_screen(self):
        pass

