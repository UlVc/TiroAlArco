import pygame
import SpriteSheet
import math

class projectile(object):
    def __init__(self, image):
        self.image = image

    def draw(self, screen, x, y, facing):
        x += 20
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, 8, 8)
        left = [0]
        right = [32]

        if facing > 0:
            sprite_sheet.draw(screen, right[0], x, y)
        else:
            sprite_sheet.draw(screen, left[0], x, y)

    def draw_guide(self, screen, color, x, y, ang, v0):
        x += 30
        y += 40
        w, z = x + v0 * 10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))
        x, y, w, z = int(x), int(y), int(w), int(z)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))