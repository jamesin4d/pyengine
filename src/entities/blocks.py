# Created by a human
# when:
# 10/26/2015
# 4:16 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from base import *

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Solid(Block):
    def __init__(self):
        Block.__init__(self)