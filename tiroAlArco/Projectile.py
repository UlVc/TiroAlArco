import pygame
import SpriteSheet

class projectile(object):
    def __init__(self, x, y, image, facing):
        self.x = x
        self.y = y - 140
        self.image = image
        self.facing = facing
        self.velocity = 8  * facing
        self.walk_count = 0
        self.left = False
        self.right = False

    def draw(self, screen, image):
        sprite_sheet = SpriteSheet.SpriteSheet('images/sprites/arrow.png', 4, 1)
        left = [1]
        right = [3]

        if self.facing > 0:
            sprite_sheet.draw(screen, right[0], self.x, self.y)
        else:
            sprite_sheet.draw(screen, left[0], self.x, self.y)