# Created by a human
# when:
# 11/4/2015
# 5:11 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from quick_map import *
from ..utilities.camera import *

class Scene(object):
    map_file = None
    map_dict = None
    map_rect = None
    solids = None
    background = None
    foreground = None
    cell_width = None
    cell_height = None
    enemy_list = None
    item_list = None
    player = None
    camera = None
    next_scene = None
    previous_scene = None

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.canvas = pygame.Surface(self.screen.get_width(), self.screen.get_height())
        self.canvas.fill((50,50,50))
        self.canvas_rect = self.canvas.get_rect()
        self.enemy_list = []
        self.item_list = []

    def get_map_information(self):
        self.map_dict = quickmap(self.map_file)
        d = self.map_dict
        self.map_rect = d['map_rect']
        self.solids = d['collision']
        self.foreground = d['foreground']
        self.background = d['background']
        self.cell_width = d['tilewidth']
        self.cell_height = d['tileheight']
        self.camera = Camera(complex_camera, self.map_rect)

    def check_level_collisions(self):
        self.camera.update(self.player)
        self.player.update()
        if self.player.rect.x > self.map_rect[0]:
            self.load_next_scene()
        if self.player.rect.x < 0:
            self.load_previous_scene()


    def load_next_scene(self):
        return self.next_scene

    def load_previous_scene(self):
        return self.previous_scene

    def update_screen(self):
        for b in self.background:
            self.screen.blit(b.image, self.camera.apply(b))
        for f in self.foreground:
            self.screen.blit(f.image, self.camera.apply(f))
        for c in self.solids:
            self.screen.blit(c.image, self.camera.apply(c))
        for i in self.item_list:
            self.screen.blit(i.image, self.camera.apply(i))
        for e in self.enemy_list:
            self.screen.blit(e.image, self.camera.apply(e))
        self.screen.blit(self.player.image, self.camera.apply(self.player))

