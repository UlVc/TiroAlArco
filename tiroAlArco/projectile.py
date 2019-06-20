import pygame
import sprite_sheet
import math

class Projectile(object):
    def __init__(self, sprite, columns, rows, image, projectile_animation=[]):
        self.sprite = sprite
        self.columns = columns
        self.rows = rows
        self.draw_projectile = True
        self.image = image
        self.projectile_animation = projectile_animation
        self.count = -1

    def draw(self, screen, (x, y), angle, vx, vy, projectile_motion, enemy):
        x += 20
        frame = sprite_sheet.SpriteSheet(self.sprite, self.columns, self.rows)
        intern_angle = math.atan2(vy, vx) * (180.0/math.pi)
        animation = self.projectile_animation != []

        if animation:
            if self.count < len(self.projectile_animation) - 1:
                self.count += 1
            else:
                self.count = 0

        enemy_rect = pygame.Rect(enemy.hitbox[0] + enemy.x, enemy.hitbox[1] + enemy.y, enemy.hitbox[2], enemy.hitbox[3])

        if enemy_rect.collidepoint(projectile_motion.x + 25, projectile_motion.y + 25):
            projectile_motion.restart_shoot()
            enemy.hit()

        if animation:
            frame.draw_rotated(screen, (x, y), intern_angle, self.projectile_animation[self.count])
        else:
            frame.draw_rotated(screen, (x, y), intern_angle, self.image)

    def draw_guide(self, screen, color, (x, y), ang, v0):
        x += 30
        y += 40
        w, z = x + v0*10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))

        pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))