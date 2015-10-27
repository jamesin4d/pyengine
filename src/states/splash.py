# Created by a human
# when:
# 10/27/2015
# 6:18 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from title import Title
from ..utilities import timer
from ..utilities import image_handling
import pygame

class SplashScreen(State):
    def __init__(self):
        State.__init__(self)
        self.next_state = Title()
        self.screen.fill((125,125,125))
        self.timer = timer.Timer(2)
        self.image = image_handling.get_image('img/splashscreen/splash.png')
        self.alpha = 0
        self.image.set_alpha(0)
        self.image = pygame.transform.scale(self.image, self.screen.get_size())
        self.img_pos = image_handling.center(self.image.get_size(), self.screen.get_size())
        self.fade = False
        self.upscreen = True


    def check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.VIDEORESIZE:
                self.image = pygame.transform.scale(self.image, (e.w, e.h))
                self.screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            if e.type == pygame.QUIT:
                self.close_game()
# any key skips it, cause I really hate when you cant skip things
            if e.type == pygame.KEYDOWN:
                self.quit()

    def tick(self):
        self.clock.tick(30)
# this is where the timer comes in, any value is fine
        if self.timer.update():
            if not self.fade:
# the real control in how long the splash screen lasts is here, in the alpha
                self.alpha += 6
                self.image.set_alpha(self.alpha)
                self.upscreen = True
                if self.alpha > 255:
                    self.fade = True
            else:
                self.alpha -= 6
                self.image.set_alpha(self.alpha)
                self.upscreen = True
                if self.alpha < -100:
                    self.quit()

    def update_screen(self):
        if self.upscreen:
#            makes sure the screen stays black
            self.screen.fill((0,0,0))
            self.screen.blit(self.image, self.img_pos)
            pygame.display.update()

    def quit(self):
        State.quit(self)