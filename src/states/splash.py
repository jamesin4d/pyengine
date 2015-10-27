# Created by a human
# when:
# 10/27/2015
# 6:18 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from game import Game
from ..utilities import timer
import pygame

class SplashScreen(State):
    def __init__(self):
        State.__init__(self)
        self.next_state = Game()
        self.timer = timer.Timer(10)

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.quit()

    def update_screen(self):
        pass