# Created by a human
# when:
# 11/3/2015
# 2:54 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from title import Title
from ..utilities import image_handling, graphicaluserinterface
import pygame


class Register(State):
    def __init__(self):
        State.__init__(self)
        self.canvas = image_handling.get_image('img/register/canvas.png')
        self.canvas = pygame.transform.scale(self.canvas, self.screen.get_size())
        self.canvas_pos = image_handling.center(self.canvas.get_size(), self.screen.get_size())
