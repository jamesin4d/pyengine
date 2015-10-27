# Created by a human
# when:
# 10/27/2015
# 9:31 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame

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


class Widget(pygame.Surface):
    def __init__(self, size, image=None):
        pygame.Surface.__init__(self, size)
        self.image = image
        self.size = size
        self.screen = pygame.display.get_surface()
        self.rect = self.get_rect()

    def set_position(self, pos):
        self.rect.topleft = pos

    def get_position(self):
        return self.rect.topleft

    def draw(self):
        if self.image is None:
            self.screen.blit(self, self.rect)
        else: self.screen.blit(self.image, self.rect)
        pygame.display.update(self.rect)


class Score(Widget):
    def __init__(self, title="", digits=8, size=18):
        self.color = (183,0,0)
        self.font = pygame.font.Font(None,size)
        self.title = title
        self.score = 0
        self.digits = digits
        self.text = title
        self.image = self.gen_image()
        Widget.__init__(self, self.image.get_size())
        self.fill((0,0,0))
        self.blit(self.gen_image(), (0,0))


    def gen_image(self):
        score = str(self.score)
        zeroes = "0" * (self.digits - len(score))
        msg = self.title + zeroes + score
        self.text = msg
        return self.font.render(msg, 0, self.color, (0,0,0))

    def update(self, score):
        self.score = score
        self.fill((0,0,0))
        self.blit(self.gen_image(), (0,0))
        self.draw()