class Abstract(object):
    def __init__(self, walk_left, walk_right, x, y, width, height, image, columns, rows):
        self.walk_left = walk_left
        self.walk_right = walk_right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.columns = columns
        self.rows = rows