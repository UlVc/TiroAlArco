# -*- coding: utf-8 -*-

import pygame
import Player
import Projectile

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tiro al arco")
bg = pygame.image.load('images/background/background.jpg')
arrow = pygame.image.load('images/sprites/arrow.jpg')
player = Player.Player(15, 810, 64, 64)

def redraw_screen():
    screen.blit(bg, (0, 0))
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen, arrow)

    pygame.display.update()

def events():
    # Movement of the bullet:
    for bullet in bullets:
        if bullet.x < SCREEN_WIDTH and bullet.x > 0: # Bounds of the screen
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 1:
            bullets.append(Projectile.projectile(int(round(player.x + player.width // 2)), int(round(player.y + player.height // 2)), arrow, facing))

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x > player.velocity:
        player.x -= player.velocity
        player.left = True
        player.right = False
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x < SCREEN_WIDTH - player.width - player.velocity:
        player.x += player.velocity
        player.right = True
        player.left = False
    else:
        player.right = False
        player.left = False
        player.walk_count = 0

# Main loop
run = True
bullets = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    events()

    redraw_screen()

pygame.quit()