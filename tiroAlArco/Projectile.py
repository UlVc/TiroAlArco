import pygame
import SpriteSheet
import math

class Projectile(object):
    def __init__(self, image, columns, rows):
        self.image = image
        self.columns = columns
        self.rows = rows
        self.draw_projectile = True
        self.projectile_animation = 32

    def draw(self, screen, (x, y), angle, vx, vy, projectile_motion, enemy):
        x += 20
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows)
        intern_angle = math.atan2(vy, vx) * (180.0/math.pi)

        if self.projectile_animation < 39:
            self.projectile_animation += 1
        else:
            self.projectile_animation = 32

        if pygame.Rect(enemy.hitbox[0] + enemy.x, enemy.hitbox[1] + enemy.y, enemy.hitbox[2], enemy.hitbox[3]).collidepoint(projectile_motion.x + 25, projectile_motion.y + 25):
            projectile_motion.restart_shoot()
            enemy.hit()

        sprite_sheet.draw_rotated(screen, (x, y), intern_angle, self.projectile_animation)

    def draw_guide(self, screen, color, (x, y), ang, v0):
        x += 30
        y += 40
        w, z = x + v0 * 10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))

        pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))