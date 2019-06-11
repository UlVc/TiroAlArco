import pygame
import Projectile
import Player
import math

class projectile_motion(object):
    def __init__(self, t, dt, v0, acceleration, angle, vx, vy, GROUND_POSITION):
        self.t = t
        self.dt = dt
        self.v0 = v0
        self.acceleration = acceleration
        self.angle = angle
        self.vx = vx
        self.vy = vy
        self.GROUND_POSITION = GROUND_POSITION
        self.lock_shoot = True
        self.space_key = False
        self.x = 0
        self.y = 0
        self.x_pos = 0
        self.y_pos = 0

    def calculate_motion(self, keys, player):
        self.x = player.x
        self.y = player.y

        if self.lock_shoot: # Lock the arrow keys when the projectile is launched
            if keys[pygame.K_LEFT]:
                self.angle += 1
            if keys[pygame.K_RIGHT]: 
                self.angle -= 1
            if keys[pygame.K_UP] and self.v0 < player.force: 
                self.v0 += 1
            if keys[pygame.K_DOWN] and self.v0 > 1:
                self.v0 -= 1
            if keys[pygame.K_SPACE]:
                self.space_key = True
                self.vy0 = self.v0 * math.sin(math.radians(self.angle))
                self.lock_shoot = False
                self.x_pos = self.x
                self.y_pos = self.y

        self.vx0 = self.v0 * math.cos(math.radians(self.angle))
        self.vy = self.acceleration*self.t - self.v0*math.sin(math.radians(self.angle))

        if self.space_key: # Projectile motion
            self.y = self.y_pos - (self.vy0*self.t) + ((.5*self.acceleration) * (self.t**2))
            self.x = self.x_pos + self.vx0*self.t
            self.t += self.dt
            if self.y > self.GROUND_POSITION:
                self.y = self.GROUND_POSITION
                self.t = 0
                self.space_key = False
                self.lock_shoot = True

    def draw_motion(self, screen, projectile, player):
        if player.x == self.x or (self.x + 5) == player.x or (self.x - 5) == player.x:
            projectile.draw_guide(screen, (0, 0, 0), self.x, self.y, self.angle, self.v0)
            projectile.draw_projectile = False
        else:
            projectile.draw_projectile = True

        if projectile.draw_projectile:
            projectile.draw(screen, self.x, self.y, self.angle)