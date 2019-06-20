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

        SCREEN_WIDTH = 350
        SCREEN_HEIGHT = 420
        bg = pygame.image.load('images/background/background_submenu.jpg')

        saitama = pygame.Rect(102, 140, 66, 96)
        goku = pygame.Rect(180, 150, 62, 69)

        arrow = pygame.Rect(50, 365, 117, 20)
        fire_ball = pygame.Rect(192, 363, 54, 20)

        saitama_image = ss.SpriteSheet('images/sprites/Saitama.png', 3, 4)
        goku_image = ss.SpriteSheet('images/sprites/Goku.png', 18, 6)

        arrow_image = ss.SpriteSheet('images/sprites/arrow.png', 3, 1)
        fire_image = ss.SpriteSheet('images/sprites/fire_ball.png', 8, 8)

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

            # pygame.draw.rect(screen, (255, 255, 255), saitama)
            saitama_image.draw(screen, 1, (80, 130))

            if pygame.mouse.get_pressed()[0] and saitama.collidepoint(pygame.mouse.get_pos()):
                self.character_index = 0

            # pygame.draw.rect(screen, (255, 255, 255), goku)
            goku_image.draw(screen, 27, (160, 130))

            if pygame.mouse.get_pressed()[0] and goku.collidepoint(pygame.mouse.get_pos()):
                self.character_index = 1

            screen.blit(projectile_selection_text, (40, 270))

            # pygame.draw.rect(screen, (255, 255, 255), arrow)
            arrow_image.draw(screen, 1 , (50, 360))
            
            if pygame.mouse.get_pressed()[0] and arrow.collidepoint(pygame.mouse.get_pos()):
                self.projectile_index = 0

            # pygame.draw.rect(screen, (255, 255, 255), fire_ball)
            fire_image.draw(screen,1 , (190, 343))

            if pygame.mouse.get_pressed()[0] and fire_ball.collidepoint(pygame.mouse.get_pos()):
                self.projectile_index = 1

            pygame.display.update()

            if self.projectile_index != -1 and self.character_index != -1:
                run = False
