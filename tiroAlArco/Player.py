import SpriteSheet
import pygame
import math
from Abstract import Abstract

class Player(Abstract):
    def __init__(self, walk_left, walk_right, idle, (x, y), width, force, velocity, image, columns, rows, hitbox):
        Abstract.__init__(self, walk_left, walk_right, (x, y), image, columns, rows)
        self.width = width
        self.idle = idle
        self.force = force
        self.velocity = velocity
        self.left = False
        self.right = False
        self.walk_count = 0
        self.is_jumping = False
        self.jump_count = 10
        self.hitbox = hitbox
        self.health = 10
        self.X = self.x
        self.Y = self.y

    def draw(self, screen, scale2x=False):
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows, scale2x)

        if self.walk_count + 1 >= (len(self.walk_left)*2) + 1:
            self.walk_count = 0
            
        if self.left:
            sprite_sheet.draw(screen, self.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            sprite_sheet.draw(screen, self.walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            sprite_sheet.draw(screen, self.idle, (self.x, self.y))

        hitbox = (self.x + self.hitbox[0], self.y + self.hitbox[1], self.hitbox[2], self.hitbox[3])
        pygame.draw.rect(screen, (255, 0, 0), (hitbox[0] + 3, hitbox[1] - 20, 60, 10))
        pygame.draw.rect(screen, (0, 128, 0), (hitbox[0] + 3, hitbox[1] - 20, 60 - ((60/10) * (10-self.health)), 10))

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
                self.walk_count = 0
        else:
            if self.jump_count >= -10:
                neg = -1 if self.jump_count < 0 else 1

                self.y -= (self.jump_count**2) * (0.5*neg)
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

    def hit(self, screen):
        self.x = self.X
        self.y = self.Y
        self.health -= 1
        self.jump_count = 10
        self.is_jumping = False

        if self.health == 0:
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('You lose!', 1, (255, 0, 0))

            screen.blit(text, (800, 400))
            pygame.display.update()
            pygame.time.delay(700)
            exit()