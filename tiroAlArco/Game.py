# -*- coding: utf-8 -*-

import pygame
import Player
import Projectile
import ProjectileMotion as pm

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GROUND_POSITION = 810

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tiro al arco")
bg = pygame.image.load('images/background/background.jpg')

walk_left_player = [3, 4, 5]
walk_right_player = [6, 7, 8]
idle_player = 1
FORCE_PLAYER = 100
VELOCITY_PLAYER = 5

player = Player.Player(walk_left_player, walk_right_player, idle_player, 15, GROUND_POSITION, 64, 64, FORCE_PLAYER, VELOCITY_PLAYER, 'images/sprites/Saitama.png', 3, 4)
projectile = Projectile.projectile('images/sprites/fire_ball.png', 8, 8)
projectile_motion = pm.ProjectileMotion(0.0, 0.5, 25.0, 1.0, 45.0, 0, 0, GROUND_POSITION)

clock = pygame.time.Clock()

def redraw_screen():
    screen.blit(bg, (0, 0))

    projectile_motion.draw_motion(screen, projectile, player)
    player.draw(screen)

    pygame.display.update()

# Main loop
while 1:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    projectile_motion.calculate_motion(keys, player)
    player.movements(keys, SCREEN_WIDTH)

    redraw_screen()