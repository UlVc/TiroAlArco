# -*- coding: utf-8 -*-

import pygame
import Player

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tiro al arco")
bg = pygame.image.load('images/background/background.jpg')
player = Player.Player(15, 810, 64, 64)

# Main loop
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.velocity: # If the user press the left arrow and we don´t wanna a position less than zero
        player.x -= player.velocity
        player.left = True
        player.right = False
    elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.width - player.velocity:
    	player.x += player.velocity
        player.right = True
        player.left = False
    else:
        player.right = False
        player.left = False
        player.walk_count = 0

    screen.blit(bg, (0, 0))
    player.draw(screen)
    pygame.display.update();

pygame.quit()