import pygame
import sys
import time

import boss_fight_functions as bff
from ship import Ship
from player_bullet import Bullet
from boss import Boss
from boss_bullet import Bossbullet



width = 1280
height = 720
clock = pygame.time.Clock()
win = pygame.display.set_mode((width,height))

pygame.init()

clock = pygame.time.Clock()


def main(win,char,stage):

	#main function for the boss fight
	plane = Ship()
	bullets = []
	alienbullets = []
	the_boss = Boss(stage)

	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(120)
		bff.gameloop(plane,clock,win,bullets)
		the_boss.bossmove(the_boss,alienbullets)
		run = bff.updategamedisp(plane,win,bullets,the_boss,alienbullets,stage,char)

	    



    



 
