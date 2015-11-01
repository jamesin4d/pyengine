# Created by a human
# when:
# 10/27/2015
# 9:29 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from game import Game
from ..utilities import image_handling, graphicaluserinterface
import pygame


class Title(State):
    def __init__(self):
        State.__init__(self)

        self.canvas = image_handling.get_image('img/titlescreen/title.png')
        self.next_state = Game()
        self.canvas = pygame.transform.scale(self.canvas, self.screen.get_size())
        self.canvas_pos = image_handling.center(self.canvas.get_size(), self.screen.get_size())
        self.set_up_user_interface()


    def set_up_user_interface(self):
        logo = image_handling.get_image('img/titlescreen/titlelogo.png')
        logo_pos = (300,10)
        self.canvas.blit(logo,logo_pos)
        load = image_handling.get_image('img/titlescreen/load.png')
        load_pos = (650,315)
        self.canvas.blit(load,load_pos)
        new = image_handling.get_image('img/titlescreen/new.png')
        new_pos = (650,270)
        self.canvas.blit(new,new_pos)
        option = image_handling.get_image('img/titlescreen/option.png')
        option_pos = (650,360)
        self.canvas.blit(option,option_pos)
        quit = image_handling.get_image('img/titlescreen/quit.png')
        quit_pos = (650,405)
        self.canvas.blit(quit,quit_pos)



    def check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.VIDEORESIZE:
                self.canvas = pygame.transform.scale(self.canvas, (e.w, e.h))
                self.screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            if e.type == pygame.QUIT:
                self.close_game()


    def update_screen(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.canvas, self.canvas_pos)
        pygame.display.update()

    def quit(self):
        State.quit(self)