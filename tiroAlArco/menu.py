# -*- coding: utf-8 -*-

from redraw_screen import game

print('Choose your character:')
print('Option 1: Saitama')
print('Option 2: Goku')
opcion = int(input()) - 1

Game.start(opcion)