import pygame
import SpriteSheet

class enemy(object):
    def __init__(self, walk_left, walk_right, x, y, width, height, end, image, columns, rows):
        self.walk_left = walk_left
        self.walk_right = walk_right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.image = image
        self.columns = columns
        self.rows = rows
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.velocity = 3

    def draw(self, screen):
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows, True)

        self.move()

        if self.walk_count + 1 >= (len(self.walk_left))*3:
            self.walk_count = 0

        if self.velocity > 0: 
            sprite_sheet.draw(screen, self.walk_right[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        else:
            sprite_sheet.draw(screen, self.walk_left[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1

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