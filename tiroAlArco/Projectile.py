import pygame
import SpriteSheet
import math

class Projectile(object):
    def __init__(self, image, columns, rows):
        self.image = image
        self.columns = columns
        self.rows = rows
        self.draw_projectile = True

    def draw(self, screen, (x, y), angle, vx, vy, projectile_motion, enemy):
        x += 20
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows)
        intern_angle = math.atan2(vy, vx) * (180.0/math.pi)

        if projectile_motion.y + 25 >= enemy.y + enemy.hitbox[1] and projectile_motion.y + 25 <= (enemy.y+enemy.hitbox[1]) + enemy.hitbox[3]:
            if projectile_motion.x + 25 >= enemy.hitbox[0] + enemy.x:
                projectile_motion.restart_shoot()

        sprite_sheet.draw_rotated(screen, 32, (x, y), intern_angle)

    def draw_guide(self, screen, color, (x, y), ang, v0):
        x += 30
        y += 40
        w, z = x + v0 * 10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))
        x, y, w, z = int(x), int(y), int(w), int(z)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))