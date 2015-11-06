# Created by a human
# when:
# 11/3/2015
# 6:07 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
# --------------------------------------------------------------------
import json
import pygame
from ..entities import blocks

# quick map method; takes a filename argument and returns a dictionary of map sprites
def quickmap(filename):
    map_dictionary = json.loads(open(filename).read())
    rows = map_dictionary["height"]
    columns = map_dictionary["width"]
    tileheight = map_dictionary["tileheight"]
    tilewidth = map_dictionary["tilewidth"]
    map_rect = (columns*tilewidth, rows*tileheight)

    layers = map_dictionary["layers"]
    tilesets = map_dictionary["tilesets"]
    all_tiles = gather_images_from_set(tilesets)

    collision, back, fore = populate_sprite_lists(layers, all_tiles, tileheight, tilewidth)
    quickmap_dictionary = {
        'map_rect': map_rect,
        'collision': collision,
        'background': back,
        'foreground': fore,
        'tileheight': tileheight,
        'tilewidth': tilewidth
    }
    return quickmap_dictionary

def gather_images_from_set(tileset):
    all_tiles = {}
    img = tileset[0]["image"]
    tile_id = tileset[0]["firstgid"]
    ih = tileset[0]["imageheight"]
    iw = tileset[0]["imagewidth"]
    th = tileset[0]["tileheight"]
    tw = tileset[0]["tilewidth"]
    set_surf = pygame.image.load('maps/' + img)
    set_surf.set_colorkey((255,255,255))
    for y in range(0,ih,th): #(start:0, range:imageheight, step: tileheight)
        for x in range(0,iw,tw):
            r = pygame.Rect(x,y,tw,th)
            tile = set_surf.subsurface(r)
            all_tiles[tile_id] = tile
            tile_id += 1
    return all_tiles

def populate_sprite_lists(layers, all_tiles, tw, th):
    collision_list = []
    foreground = []
    background = []
    for layer in layers:
        collision = False
        fore = False
        back = False
        if 'properties' in layer:
            properties = layer['properties']
            if 's' in properties:
                collision = True
            if 'f' in properties:
                fore = True
            if 'b' in properties:
                back = True
        data = layer['data']
        index = 0
        for y in range(0, layer['height']):
            for x in range(0, layer['width']):
                id_key = data[index]
                if id_key != 0:
                    if collision:
                        solid = blocks.Solid()
                        solid.rect = pygame.Rect(x*tw, y*th, tw, th)
                        solid.image = all_tiles[id_key]
                        collision_list.append(solid)
                    if fore:
                        fgBlock = blocks.Block()
                        fgBlock.rect = pygame.Rect(x*tw, y*th, tw, th)
                        fgBlock.image = all_tiles[id_key]
                        foreground.append(fgBlock)
                    if back:
                        bgBlock = blocks.Block()
                        bgBlock.rect = pygame.Rect(x*tw, y*th, tw, th)
                        bgBlock.image = all_tiles[id_key]
                        background.append(bgBlock)
                index += 1
    return collision_list, foreground, background