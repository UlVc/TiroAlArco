import pygame

class SpriteSheet(object):
    def __init__(self, image, columns, rows, scale=False):
        self.sheet = pygame.image.load(image)

        if scale:
            self.sheet = pygame.transform.scale2x(self.sheet)
            
        self.columns = columns
        self.rows = rows
        self.total_cell_count = columns * rows
        self.rect = self.sheet.get_rect()

        width = self.cell_width = self.rect.width / columns
        height = self.cell_height = self.rect.height / rows

        self.cells = list([(index % columns*width, index / columns*height, width, height) for index in range(self.total_cell_count)])

    def draw(self, surface, cell_index, (x, y)):
        sub_surface = self.sheet.subsurface(self.cells[cell_index])
        surface.blit(sub_surface, (x, y))

    def draw_rotated(self, surface, (x, y), angle, projectile_animation):

        sub_surface = self.sheet.subsurface(self.cells[projectile_animation])
        self.image_rotated = pygame.transform.rotate(sub_surface, angle)

        surface.blit(self.image_rotated, (x, y))