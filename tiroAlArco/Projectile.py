import pygame
import SpriteSheet
import math

class Projectile(object):
    def __init__(self, image, columns, rows):
        self.image = image
        self.columns = columns
        self.rows = rows

    def draw(self, screen, x, y, angle):
        x += 20
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows)
        left = [0]
        right = [32]

        sprite_sheet.draw_rotated(screen, right[0], x, y, angle)

    def draw_guide(self, screen, color, x, y, ang, v0):
        x += 30
        y += 40
        w, z = x + v0 * 10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))
        x, y, w, z = int(x), int(y), int(w), int(z)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))