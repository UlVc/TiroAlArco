class Abstract(object):
    def __init__(self, walk_left, walk_right, (x, y), image, columns, rows):
        self.walk_left = walk_left
        self.walk_right = walk_right
        self.x = x
        self.y = y
        self.image = image
        self.columns = columns
        self.rows = rows

    def draw(self):
        pass

    def move(self):
        pass