# Created by a human
# when:
# 10/27/2015
# 9:29 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from ..eng import State
from game import Game
from new_game import  Register
from ..utilities import image_handling, graphicaluserinterface, debugger
import pygame


class Title(State):
    logo = None
    new_game_button = None
    load_game_button = None
    options_button = None
    quit_button = None
    user_interface = []
    def __init__(self):
        State.__init__(self)
        self.canvas = image_handling.get_image('img/titlescreen/title.png')
        self.next_state = Game()
        self.canvas = pygame.transform.scale(self.canvas, self.screen.get_size())
        self.canvas_pos = image_handling.center(self.canvas.get_size(), self.screen.get_size())
        self.set_up_user_interface()


    def set_up_user_interface(self):
        logo = image_handling.get_image('img/titlescreen/titlelogo.png')
        logo_pos = (150,10)
        self.logo = graphicaluserinterface.Button(logo,logo_pos)
        self.user_interface.append(self.logo)

        load = image_handling.get_image('img/titlescreen/load.png')
        load_pos = (550,315)
        self.load_game_button = graphicaluserinterface.Button(load,load_pos)
        self.user_interface.append(self.load_game_button)

        new = image_handling.get_image('img/titlescreen/new.png')
        new_pos = (550,270)
        self.new_game_button = graphicaluserinterface.Button(new,new_pos)
        self.user_interface.append(self.new_game_button)

        option = image_handling.get_image('img/titlescreen/option.png')
        option_pos = (550,360)
        self.options_button = graphicaluserinterface.Button(option,option_pos)
        self.user_interface.append(self.options_button)

        quit = image_handling.get_image('img/titlescreen/quit.png')
        quit_pos = (550,405)
        self.quit_button = graphicaluserinterface.Button(quit,quit_pos)
        self.user_interface.append(self.quit_button)

        for g in self.user_interface:
            self.canvas.blit(g.image, g.position)


    def check_events(self):
        for g in self.user_interface:
            g.check_mouse()

        if self.new_game_button.clicked_on:
            self.next_state = Game()
            self.quit()
        if self.load_game_button.clicked_on:
            self.next_state = Game()
            self.quit()
        if self.quit_button.clicked_on:
            self.close_game()

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