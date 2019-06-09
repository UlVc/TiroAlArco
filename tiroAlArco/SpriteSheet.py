import pygame

class SpriteSheet(object):
    def __init__(self, filename, columns, rows):
        self.sheet = pygame.image.load(filename)
        self.columns = columns
        self.rows = rows
        self.totalCellCount = columns * rows
        self.rect = self.sheet.get_rect()

        width = self.cellWidth = self.rect.width / columns
        height = self.cellHeight = self.rect.height / rows

        self.cells = list([(index % columns * width, index / columns * height, width, height) for index in range(self.totalCellCount)])

    def draw(self, surface, cellIndex, x, y):
        surface.blit(self.sheet, (x, y), self.cells[cellIndex])