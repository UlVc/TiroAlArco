# -*- coding: utf-8 -*-
# 
def printos(surface, text, x, y, color, font):
    text_in_lines = text.split('\n')
    for line in text_in_lines:
        new = font.render(line, 1, color)
        surface.blit(new, (x, y))
        y += new.get_height()

import pygame
import Player
import Projectile
import math
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
projectile_motion = pm.projectile_motion(0.0, 0.5, 25.0, 1.0, 45.0, 0, 0, GROUND_POSITION)

clock = pygame.time.Clock()

def redraw_screen():
    screen.blit(bg, (0, 0))

    #printos(screen, "x = %d y = %d ang = %d v0 = %d vx = %d vy = %d"%(x, y, ang, v0, vx0, vy), 0, 0, (0, 0, 0), pygame.font.Font(None, 30) )

    projectile_motion.draw_motion(screen, projectile, player)

    player.draw(screen)

    pygame.display.update()

def movements(player):
    if keys[pygame.K_a] and player.x > player.velocity:
        player.x -= player.velocity
        player.left = True
        player.right = False
    elif keys[pygame.K_d] and player.x < SCREEN_WIDTH - player.width - player.velocity:
        player.x += player.velocity
        player.right = True
        player.left = False
    else:
        player.right = False
        player.left = False
        player.walk_count = 0

    if not(player.is_jumping):
        if keys[pygame.K_w]:
            player.is_jumping = True
            right = False
            left = False
            walkCount = 0
    else:
        if player.jump_count >= -10:
            neg = 1
            if player.jump_count < 0:
                neg = -1
            player.y -= (player.jump_count ** 2) * 0.5 * neg
            player.jump_count -= 1
        else:
            player.is_jumping = False
            player.jump_count = 10

# Main loop
while 1:
    clock.tick(30)

    x = player.x
    y = player.y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    projectile_motion.calculate_motion(keys, player)

    movements(player)

    redraw_screen()