import pygame
import Player

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tiro al arco")

player = Player.player(300, 410, 64, 64)

# Main loop
game_over = True
while not game_over: 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    man.draw(win)
    pygame.display.update();

pygame.quit()