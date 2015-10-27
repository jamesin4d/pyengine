# Created by a human
# when:
# 10/27/2015
# 9:29 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from game import Game
from ..utilities import timer
from ..utilities import image_handling
import pygame


class Title(State):
    def __init__(self):
        State.__init__(self)