import SpriteSheet

class Player(object):
    def __init__(self, walk_left, walk_right, idle, x, y, width, height, image, columns, rows):
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.walk_count = 0
        self.image = image
        self.columns = columns
        self.rows = rows
        self.walk_left = walk_left
        self.walk_right = walk_right
        self.idle = idle

    def draw(self, screen):
        sprite_sheet = SpriteSheet.SpriteSheet(self.image, self.columns, self.rows)

        if self.walk_count + 1 >= (len(self.walk_left)*2) + 1:
            self.walk_count = 0
        if self.left:
            sprite_sheet.draw(screen, self.walk_left[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        elif self.right:
            sprite_sheet.draw(screen, self.walk_right[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        else:
            sprite_sheet.draw(screen, self.idle, self.x, self.y)