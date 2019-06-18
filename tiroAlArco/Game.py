# -*- coding: utf-8 -*-

import pygame
import json
import Player
import Projectile
import ProjectileMotion
import Mob

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

with open('stats/mobs_stats.json') as file_mobs, open('stats/character_stats.json') as file_characters:
    data_enemies = json.load(file_mobs)
    data_characters = json.load(file_characters)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GROUND_POSITION = 840

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tiro al arco")
bg = pygame.image.load('images/background/background.jpg')

enemy = Mob.Mob(data_enemies[0]['walk_left'], data_enemies[0]['walk_right'], (data_enemies[0]['x'], data_enemies[0]['y']), 
                data_enemies[0]['image'], data_enemies[0]['columns'], data_enemies[0]['rows'], data_enemies[0]['end'], data_enemies[0]['hitbox'])
player = Player.Player(data_characters[0]['walk_left'], data_characters[0]['walk_right'], data_characters[0]['idle'], (data_characters[0]['x'], 
                       data_characters[0]['y']), data_characters[0]['width'], data_characters[0]['force'], data_characters[0]['velocity'], 
                       data_characters[0]['image'], data_characters[0]['columns'], data_characters[0]['rows'], data_characters[0]['hitbox'])
projectile = Projectile.Projectile('images/sprites/fire_ball.png', 8, 8)
projectile_motion = ProjectileMotion.ProjectileMotion(screen, 0.0, 0.5, 25.0, 1.0, 45.0, 0, 0, GROUND_POSITION, 'sounds/arrow_release.wav')

clock = pygame.time.Clock()

def redraw_screen():
    screen.blit(bg, (0, 0))

    if (player.x == projectile_motion.x or (projectile_motion.x + 5) == player.x or (projectile_motion.x - 5) == player.x) and not(projectile_motion.shoot):
        projectile.draw_guide(screen, (0, 0, 0), (player.x, player.y), projectile_motion.angle, projectile_motion.v0)

    if projectile_motion.shoot:
        projectile.draw(screen, (projectile_motion.x, projectile_motion.y), projectile_motion.angle, projectile_motion.vx, projectile_motion.vy, projectile_motion, enemy)

    if enemy.health > 0:
        collision_enemy_character()
         
    player.draw(screen)
    enemy.draw(screen)

    pygame.display.update()

def collision_enemy_character():
    enemy_rect = pygame.Rect(enemy.hitbox[0] + enemy.x, enemy.hitbox[1] + enemy.y, enemy.hitbox[2], enemy.hitbox[3])
    player_rect = pygame.Rect(player.hitbox[0] + player.x, player.hitbox[1] + player.y, player.hitbox[2], player.hitbox[3])
    
    if enemy_rect.colliderect(player_rect):
        player.hit(screen)
        enemy.restart_position()

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