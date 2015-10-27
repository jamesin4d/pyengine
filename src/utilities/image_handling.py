# Created by a human
# when:
# 10/26/2015
# 4:02 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame


def color(r, g, b):
    return pygame.Color((r, g, b))


def rect(x, y, w, h):
    return pygame.Rect(x, y, w, h)


def get_image(image):
    img = pygame.image.load(image).convert()
    img.set_colorkey((255, 255, 255))
    return img


def center(img_size, surf_size):
    img_x, img_y = img_size
    sur_x, sur_y = surf_size
    cen_x = sur_x/2 - img_x/2
    cen_y = sur_y/2 - img_y/2
    return [cen_x, cen_y]


def strip_sheet_no_convert(filename, sheet_x, sheet_y, image_x, image_y):
    frames = []
    sprite_sheet = pygame.image.load(filename)
    sprite_sheet.set_colorkey((255,255,255))
    sheet_width = sheet_x
    sheet_height = sheet_y
    img_width = image_x
    img_height = image_y
    for y in range(0, sheet_height, img_height):
        for x in range(0, sheet_width, img_width):
            r = pygame.Rect(x, y, img_width, img_height)
            t = sprite_sheet.subsurface(r)
            frames.append(t)
    return frames

def strip_sheet(filename,sheet_x,sheet_y,image_x,image_y):
        frames = []
        sprite_sheet = pygame.image.load(filename).convert()
        sprite_sheet.set_colorkey((255,255,255))
        sheet_width = sheet_x
        sheet_height = sheet_y
        img_width = image_x
        img_height = image_y
        for y in range(0, sheet_height, img_height):
            for x in range(0, sheet_width, img_width):
                r = pygame.Rect(x,y,img_width, img_height)
                t = sprite_sheet.subsurface(r)
                frames.append(t)
        return frames