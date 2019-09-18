import pygame
import random
import time
import sys

import menus as menu
import playerfunctions as pf

from mosquito import Mosquito
from hand import Hand

#initalises pygame
pygame.init()

#checks if a save file already exists
pf.check_new()

#checks the currently equipped cursor
equipped = pf.cur_cursor()

#sets window and caption
win = pygame.display.set_mode((1280,700))
pygame.display.set_caption("Mosquito Hunter Generations Ultimate")
  

char = Hand(equipped)

x = True


while x:
    #opens the start menu
    menu.startmenu(win,char)
pygame.quit()
    
