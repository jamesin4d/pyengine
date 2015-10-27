# Created by a human
# when:
# 10/26/2015
# 3:55 PM
#
#
# --------------------------------------------------------------------
import pygame


class Base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def collision_test(self):
        pass

    def update_status(self):
        pass

    def update_onscreen(self):
        pass

