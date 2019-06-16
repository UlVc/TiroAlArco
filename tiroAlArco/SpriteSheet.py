import pygame

class SpriteSheet(object):
    def __init__(self, image, columns, rows, scale=False):
        self.sheet = pygame.image.load(image)

        if scale:
            self.sheet = pygame.transform.scale2x(self.sheet)
            
        self.columns = columns
        self.rows = rows
        self.totalCellCount = columns * rows
        self.rect = self.sheet.get_rect()

        width = self.cellWidth = self.rect.width / columns
        height = self.cellHeight = self.rect.height / rows

        self.cells = list([(index % columns*width, index / columns*height, width, height) for index in range(self.totalCellCount)])

    def draw(self, surface, cellIndex, (x, y)):
        sub_surface = self.sheet.subsurface(self.cells[cellIndex])
        surface.blit(sub_surface, (x, y))

    def draw_rotated(self, surface, cellIndex, (x, y), angle):
        sub_surface = self.sheet.subsurface(self.cells[cellIndex])
        self.image_rotated = pygame.transform.rotate(sub_surface, angle)
        surface.blit(self.image_rotated, (x, y))