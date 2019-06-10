# -*- coding: utf-8 -*-
# 
def printos(screen, text, x, y, color, font, v0):
    text_in_lines = text.split('\n')

    for line in text_in_lines:
        new = font.render(line, 1, color)
        screen.blit(new, (x, y))
        y += new.get_height()
 
def arrow(screen, color, x, y, ang):
    pygame.draw.line(screen, color, (x, y), (x + 20*math.cos(math.radians(ang + 150.0)), y - 20*math.sin(math.radians(ang + 150.0))))
    pygame.draw.line(screen, color, (x, y), (x + 20*math.cos(math.radians(ang + 210.0)), y - 20*math.sin(math.radians(ang + 210.0))))
 
def vector(screen, color, x, y, ang, v0):
    w, z = x + v0 * 10*math.cos(math.radians(ang)), y - v0*10*math.sin(math.radians(ang))
    x, y, w, z = int(x), int(y), int(w), int(z)
    # arrow(screen, color, w, z, ang)
    pygame.draw.line(screen, (0, 0, 0), (x, y), (w, z))

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
arrow = pygame.image.load('images/sprites/arrow.jpg')
player = Player.Player(15, 810, 64, 64)
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
font = pygame.font.Font(None, 30) 
blue = (0, 0, 255)

clock = pygame.time.Clock()

def redraw_screen():
    screen.blit(bg, (0, 0))
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen, arrow)

    pygame.display.update()

def events():
    

    # Movement of the bullet:
    '''
    for bullet in bullets:
        if bullet.x < SCREEN_WIDTH and bullet.x > 0: # Bounds of the screen
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    '''


    # if keys[pygame.K_SPACE]:
    '''
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 1:
            bullets.append(Projectile.projectile(int(round(player.x + player.width // 2)), int(round(player.y + player.height // 2)), arrow, facing))
    '''
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ang += 1
        if(ang >= 90):
            ang = 90
    if keys[pygame.K_DOWN]: 
        ang -= 1
        if(ang < 0):
            ang = 0
    if keys[pygame.K_RIGHT] and v0 < 100: 
        v0 += 1
    if keys[pygame.K_LEFT] and v0 > 1:
        v0 -= 1
    if keys[pygame.K_SPACE]:
        lock = False
        lock1 = True
        vy0 = v0 * math.sin(math.radians(ang))

    vx0 = v0 * math.cos(math.radians(ang))
    vy = a*t - v0*math.sin(math.radians(ang))

    if lock1:
        y = (SCREEN_HEIGHT-radio) - (vy0*t) + ((.5*a) * (t**2))
        x = radio + vx0*t
        t += dt
        if y > (SCREEN_HEIGHT - radio):
            y = SCREEN_HEIGHT - radio
            t = 0
            lock1 = False

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

    screen.blit(bg, (0, 0))
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen, arrow)

    printos(screen, "x = %d y = %d ang = %d v0 = %d vx = %d vy = %d"%(x - radio, SCREEN_HEIGHT - radio - y, ang, v0, vx0, vy), 0, 0, (0, 0, 0), font, v0)
    pygame.draw.circle(screen, blue, (int(x), int(y)), radio) 
    vector(screen, blue, x, y, ang, v0)

    pygame.display.update()

# Main loop
run = True
bullets = []
lock_shoot = False
while run:
    x = player.x
    y = player.y

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ang += 1
    if keys[pygame.K_DOWN]: 
        ang -= 1
        if(ang < 0):
            ang = 0
    if keys[pygame.K_RIGHT] and v0 < 100: 
        v0 += 1
    if keys[pygame.K_LEFT] and v0 > 1:
        v0 -= 1
    if keys[pygame.K_SPACE]:
        lock1 = True
        vy0 = v0 * math.sin(math.radians(ang))

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

    screen.blit(bg, (0, 0))
    player.draw(screen)

    #for bullet in bullets:
    #    bullet.draw(screen, arrow)

    printos(screen, "x = %d y = %d ang = %d v0 = %d vx = %d vy = %d"%(x - radio, SCREEN_HEIGHT - radio - y, ang, v0, vx0, vy), 0, 0, (0, 0, 0), font, v0)
    pygame.draw.circle(screen, blue, (int(x), int(y)), radio) 
    vector(screen, blue, x, y, ang, v0)

    pygame.display.update()
    clock.tick(30)

pygame.quit()