import pygame
import SpriteSheet
import math

class projectile(object):
    def __init__(self, image):
        self.image = image

    def draw(self, screen, x, y, facing):
        y = y - 140
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, 4, 1)
        left = [1]
        right = [3]

        if facing > 0:
            sprite_sheet.draw(screen, right[0], x, y)
        else:
            sprite_sheet.draw(screen, left[0], x, y)

    def draw_guide(self, screen, color, x, y, ang, v0):
        w, z = x + v0 * 10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))
        x, y, w, z = int(x), int(y), int(w), int(z)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))