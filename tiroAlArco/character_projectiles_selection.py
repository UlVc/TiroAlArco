import pygame
import sprite_sheet as ss

class CharacterProjectilesSelection(object):
    def __init__(self):
        self.character_index = -1
        self.projectile_index = -1

    def start(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.init()
        pygame.font.init()

        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        character_selection_text = myfont.render('Choose your character:', True, (0, 0, 0))
        projectile_selection_text = myfont.render('Choose your projectile:', True, (0, 0, 0))

        SCREEN_WIDTH = 400
        SCREEN_HEIGHT = 500
        bg = pygame.image.load('images/background/background.jpg')

        saitama = pygame.Rect(100, 150, 64, 64)
        goku = pygame.Rect(180, 150, 64, 64)

        arrow = pygame.Rect(100, 345, 64, 64)
        fire_ball = pygame.Rect(180, 345, 64, 64)

        saitama_image = ss.SpriteSheet('images/sprites/Saitama.png', 3, 4)
        goku_image = ss.SpriteSheet('images/sprites/Goku.png', 18, 6)

        pygame.display.set_caption('Character selection')
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            mpos = pygame.mouse.get_pos()

            screen.blit(bg, (0, 0))

            screen.blit(character_selection_text, (40, 75))

            pygame.draw.rect(screen, (255, 255, 255), saitama)
            saitama_image.draw(screen, 1, (80, 130))

            if pygame.mouse.get_pressed()[0] and saitama.collidepoint(pygame.mouse.get_pos()):
                self.character_index = 0

            pygame.draw.rect(screen, (255, 255, 255), goku)
            goku_image.draw(screen, 27, (160, 130))

            if pygame.mouse.get_pressed()[0] and goku.collidepoint(pygame.mouse.get_pos()):
                self.character_index = 1

            screen.blit(projectile_selection_text, (40, 270))

            pygame.draw.rect(screen, (255, 255, 255), arrow)

            if pygame.mouse.get_pressed()[0] and arrow.collidepoint(pygame.mouse.get_pos()):
                self.projectile_index = 0

            pygame.draw.rect(screen, (255, 255, 255), fire_ball)

            if pygame.mouse.get_pressed()[0] and fire_ball.collidepoint(pygame.mouse.get_pos()):
                self.projectile_index = 1

            pygame.display.update()

            if self.projectile_index != -1 and self.character_index != -1:
                run = False
