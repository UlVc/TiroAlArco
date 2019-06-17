import pygame
import SpriteSheet
from Abstract import Abstract

class Mob(Abstract):
    def __init__(self, walk_left, walk_right, (x, y), image, columns, rows, end, hitbox):
        Abstract.__init__(self, walk_left, walk_right, (x, y), image, columns, rows)
        self.end = end
        self.hitbox = hitbox
        self.path = [x, self.end]
        self.walk_count = 0
        self.velocity = 3

    def draw(self, screen):
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows, True)

        self.move()

        if self.walk_count + 1 >= (len(self.walk_left))*3:
            self.walk_count = 0

        if self.velocity > 0: 
            sprite_sheet.draw(screen, self.walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            sprite_sheet.draw(screen, self.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        hitbox = (self.x + self.hitbox[0], self.y + self.hitbox[1], self.hitbox[2], self.hitbox[3]) # Rectangle used for hitbox
        pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walk_count = 0
        else:
            if self.x - self.velocity > self.path[0]: 
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walk_count = 0