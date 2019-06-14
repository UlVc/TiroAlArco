# -*- coding: utf-8 -*-

import pygame
import Player
import Projectile
import ProjectileMotion as pm
import Enemy

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
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

walk_left_enemy = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
walk_right_enemy = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

enemy = Enemy.enemy(walk_left_enemy, walk_right_enemy, 300, GROUND_POSITION, 64, 64, 1000, 'images/sprites/goblin.png', 11, 5)
player = Player.Player(walk_left_player, walk_right_player, idle_player, 15, GROUND_POSITION, 64, 64, FORCE_PLAYER, VELOCITY_PLAYER, 'images/sprites/Saitama.png', 3, 4)
projectile = Projectile.projectile('images/sprites/fire_ball.png', 8, 8)
projectile_motion = pm.ProjectileMotion(0.0, 0.5, 25.0, 1.0, 45.0, 0, 0, GROUND_POSITION, 'sounds/arrow_release.wav')

clock = pygame.time.Clock()

def redraw_screen():
    screen.blit(bg, (0, 0))

    if (player.x == projectile_motion.x or (projectile_motion.x + 5) == player.x or (projectile_motion.x - 5) == player.x) and not(projectile_motion.shoot):
        projectile.draw_guide(screen, (0, 0, 0), projectile_motion.x, projectile_motion.y, projectile_motion.angle, projectile_motion.v0)

    if projectile_motion.shoot:
        projectile.draw(screen, projectile_motion.x, projectile_motion.y, projectile_motion.angle)

    player.draw(screen)
    enemy.draw(screen)

    pygame.display.update()

# Main loop
while 1:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    projectile_motion.calculate_motion(keys, player)
    player.move(keys, SCREEN_WIDTH)

    redraw_screen()