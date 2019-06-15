# -*- coding: utf-8 -*-

import Game

print('Choose your character:')
print('Option 1: Saitama')
print('Option 2: Goku')
opcion = int(input()) - 1

Game.start(opcion)