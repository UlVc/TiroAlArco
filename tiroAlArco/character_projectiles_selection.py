class CharacterProjectilesSelection(object):
    def __init__(self):
        self.character_index = 0
        self.projectile_index = 0

    def character_selection(self):
        print('Select your character:')
        print('1.- Saitama')
        print('2.- Goku')
        self.character_index = int(input()) - 1

    def projectile_selection(self):
        print('Select your projectile:')
        print('1.- Arrow')
        print('2.- Fire ball')
        self.projectile_index = int(input()) - 1