# -*- coding: utf-8 -*-

import pygame
import Player
import Projectile
import math

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tiro al arco")
bg = pygame.image.load('images/background/background.jpg')

walk_left_player = [3, 4, 5]
walk_right_player = [6, 7, 8]
idle_player = 1

player = Player.Player(walk_left_player, walk_right_player, idle_player, 15, 810, 64, 64, 'images/sprites/Saitama.png', 3, 4)
projectile = Projectile.projectile('images/sprites/fire_ball.png')

radio = 10

t = 0.0
dt = 0.5
     
v0 = 25.0
a = 1.0
ang = 45.0
     
vx = 0
vy = 0

lock = True
lock1 = False

clock = pygame.time.Clock()

def redraw_screen():
    screen.blit(bg, (0, 0))

    player.draw(screen)
    
    projectile.draw(screen, x, y, facing)
    projectile.draw_guide(screen, (0, 0, 0), x, y, ang, v0)

    pygame.display.update()

def movements():
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

# Main loop
lock_shoot = True
guide = True
while 1:
    clock.tick(30)

    x = player.x
    y = player.y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if lock_shoot:
        if keys[pygame.K_LEFT]:
            ang += 1
        if keys[pygame.K_RIGHT]: 
            ang -= 1
            if(ang < 0):
                ang = 0
        if keys[pygame.K_UP] and v0 < 100: 
            v0 += 1
        if keys[pygame.K_DOWN] and v0 > 1:
            v0 -= 1
        if keys[pygame.K_SPACE]:
            lock1 = True
            vy0 = v0 * math.sin(math.radians(ang))
            guide = False
            lock_shoot = False

    vx0 = v0 * math.cos(math.radians(ang))
    vy = a*t - v0*math.sin(math.radians(ang))

    if lock1:
        y = (player.y) - (vy0*t) + ((.5*a) * (t**2))
        x = player.x + radio + vx0*t
        t += dt
        if y > player.y + 60:
            y = player.y + 60
            t = 0
            lock1 = False
            lock_shoot = True

    # Direction of the projectile:
    if ang > 90:
        facing = -1
    else:
        facing = 1

    movements()

    screen.blit(bg, (0, 0))

    player.draw(screen)
    
    projectile.draw(screen, x, y, facing)

    if player.x == x or (x + 5) == player.x or (x - 5) == player.x:
        projectile.draw_guide(screen, (0, 0, 0), x, y, ang, v0)

    pygame.display.update()