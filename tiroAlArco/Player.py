import SpriteSheet

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.walk_count = 0

    def draw(self, screen):
        sprite_sheet = SpriteSheet.SpriteSheet('images/sprites/RainbowIslandsCharacter.png', 7, 4)
        walk_left = [0, 1, 2, 3, 4]
        walk_right = [8, 9, 10, 11, 12]
        idle = 17

        if self.walk_count + 1 >= 11:
            self.walk_count = 0
        if self.left:
            sprite_sheet.draw(screen, walk_left[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        elif self.right:
            sprite_sheet.draw(screen, walk_right[self.walk_count // 3], self.x, self.y)
            self.walk_count += 1
        else:
            sprite_sheet.draw(screen, idle, self.x, self.y)