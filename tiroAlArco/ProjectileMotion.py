import pygame
import Projectile
import Player
import SpriteSheet
import math

class ProjectileMotion(object):
    def __init__(self, screen, t, dt, v0, acceleration, angle, vx, vy, GROUND_POSITION, sound_effect):
        self.screen = screen
        self.t = t
        self.dt = dt
        self.v0 = v0
        self.acceleration = acceleration
        self.angle = angle
        self.vx = vx
        self.vy = vy
        self.GROUND_POSITION = GROUND_POSITION
        self.sound_effect = sound_effect
        self.lock_shoot = True
        self.space_key = False
        self.x = 0
        self.y = 0
        self.x_pos = 0
        self.y_pos = 0
        self.shoot = False

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
            if keys[pygame.K_LCTRL]:
                self.angle = 135
            if keys[pygame.K_RCTRL]:
                self.angle = 45
            if keys[pygame.K_SPACE]:
                pygame.mixer.music.load(self.sound_effect)
                pygame.mixer.music.play()
                self.space_key = True
                self.shoot = True
                self.vy0 = self.v0 * math.sin(math.radians(self.angle))
                self.lock_shoot = False
                self.x_pos = self.x
                self.y_pos = self.y

        self.vx = self.v0 * math.cos(math.radians(self.angle))
        self.vy = self.v0*math.sin(math.radians(self.angle)) - self.acceleration*self.t

        if self.space_key: # Projectile motion
            self.y = self.y_pos - (self.vy0*self.t) + ((.5*self.acceleration) * (self.t**2))
            self.x = self.x_pos + self.vx*self.t
            self.t += self.dt

            if self.x > 2600 or self.x < -600:
                self.y = self.GROUND_POSITION + 1

            if self.y > self.GROUND_POSITION:
                self.y = self.GROUND_POSITION
                self.t = 0
                self.space_key = False
                self.lock_shoot = True
                self.shoot = False