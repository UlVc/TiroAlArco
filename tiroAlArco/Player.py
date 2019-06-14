import SpriteSheet
import pygame

class Player(object):
    def __init__(self, walk_left, walk_right, idle, x, y, width, height, force, velocity, image, columns, rows):
        self.walk_left = walk_left
        self.walk_right = walk_right
        self.idle = idle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.force = force
        self.velocity = velocity
        self.image = image
        self.columns = columns
        self.rows = rows
        self.left = False
        self.right = False
        self.walk_count = 0
        self.is_jumping = False
        self.jump_count = 10

    def draw(self, screen):
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows)

        if self.walk_count + 1 >= (len(self.walk_left)*2) + 1:
            self.walk_count = 0
            
        if self.left:
            sprite_sheet.draw(screen, self.walk_left[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        elif self.right:
            sprite_sheet.draw(screen, self.walk_right[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        else:
            sprite_sheet.draw(screen, self.idle, self.x, self.y)

    def move(self, keys, SCREEN_WIDTH):
        if keys[pygame.K_a] and self.x > self.velocity:
            self.x -= self.velocity
            self.left = True
            self.right = False
        elif keys[pygame.K_d] and self.x < SCREEN_WIDTH - self.width - self.velocity:
            self.x += self.velocity
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walk_count = 0

        if not(self.is_jumping):
            if keys[pygame.K_w]:
                self.is_jumping = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10