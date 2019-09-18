import pygame
import sys
import time
import os
import math


def check_new():

	#function to check if a save file already exists
	try:
		data = open("SaveData.txt","r+")
		data.close()
	except FileNotFoundError:
		data = open("SaveData.txt","w+") 
		data.write('Balance,0,')
		data.write('Default Hand,1,8,')
		data.write('Fire Hand,0,150,')
		data.write('Poison Hand,0,250,')
		data.write('Plus 5,0,10,')
		data.write('Slow,0,10,')
		data.write('Equipped,DH,')
		data.write('Final Boss Ticket,False,1000,')
		data.flush()                   
		os.fsync(data.fileno()) 
		data.close()

def gaingold(gold):

	#increase the gold count
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]
	del y[0][-1]

	for j in y:
		for i in range(int(len(j))+1):
			if j[i] == "Balance":
				y[0][i+1] = int(y[0][i+1]) + gold
				break
	
	#rewrites the data
	data.seek(0)
	data.truncate()
	for j in y:
		for i in j:
			data.write(str(i)+',')


	data.flush()
	os.fsync(data.fileno())
	data.close()


def losegold():

	#function ro reduce gold on a loss
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]
	del y[0][-1]

	for j in y:
		for i in range(int(len(j))+1):
			if j[i] == "Balance":
				y[0][i+1] = int(int(y[0][i+1]) * 0.92)
				break
	
	#rewrites the data
	data.seek(0)
	data.truncate()
	for j in y:
		for i in j:
			data.write(str(i)+',')


	data.flush()
	os.fsync(data.fileno())
	data.close()



def displaygold():

	#function to display the gold
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]

	for j in y:
		for i in range(int(len(j))+1):
			if j[i] == "Balance":
				gold_qt = str(j[i+1]) 
				break

	goldfont = pygame.font.SysFont('Impact',24)
	gold_amt = goldfont.render(str(gold_qt),False,(255,215,0))

	data.close()

	return gold_amt

def cur_cursor():

	#function to get the current cursor
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]

	for j in y:
		for i in range(int(len(j))+1):
			if j[i] == "Equipped":
				equipped = str(y[0][i+1]) 
				break

	data.close()
	return equipped

def getcost():
	
	#function to get the upgrade/purchase cost of each item
	upcoin = pygame.image.load('imgs/coin.png').convert_alpha()
	upcoin = pygame.transform.scale(upcoin,(20,15))
	
	gold = (255,215,0)
	
	font = pygame.font.SysFont('Impact',16)
	costfont = font.render('Cost: ',False,(255,255,255))

	x = [50,300,550,800,1050]
	
	count = 0

	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]
	if count == 0:
		for j in y:
			for i in range(int(len(j)+1)):
				if j[i] == "Default Hand":
					dhc = str(j[i+2])
				elif j[i] == "Fire Hand":
					fhc = str(j[i+2])
				elif j[i] == "Poison Hand":
					phc = str(j[i+2])
				elif j[i] == "Plus 5":
					p5c = str(j[i+2])
				elif j[i] == "Slow":
					sc = str(j[i+2])
				elif j[i] == "Final Boss Ticket":
					fbtc = str(j[i+2])
					break
			count += 1

	#creates the text for each cost
	dhct = font.render(dhc,False,gold)
	fhct = font.render(fhc,False,gold)
	phct = font.render(phc,False,gold)
	p5ct = font.render(p5c,False,gold)
	sct = font.render(sc,False,gold)
	fbtct = font.render(fbtc,False,gold)

	return dhct,fhct,phct,p5ct,sct,fbtct

