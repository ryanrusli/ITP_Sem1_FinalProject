import pygame
import os
import sys

import menus as menu
import playerfunctions as pf

from hand import Hand

def merchant_menu(win,char):

	#function for the main merchant menu displaying inventory and shop icons
	bg = pygame.image.load('backgrounds/merchant.jpg').convert_alpha()


	arrow = pygame.image.load('imgs/l_arrow.png').convert_alpha()
	arrow = pygame.transform.scale(arrow,(50,50))

	shopic = pygame.image.load('imgs/shop.png').convert_alpha()
	shopic = pygame.transform.scale(shopic,(300,300))


	invenic = pygame.image.load('imgs/inventory.png').convert_alpha()
	invenic = pygame.transform.scale(invenic,(300,192))
	
	font = pygame.font.SysFont('Impact',64)	

	shop_text = font.render('Shop',False,(255,255,255))
	inventory_text = font.render('Inventory',False,(255,255,255))

	grey = (220,220,220)        

	merch_menu = True
	while merch_menu:
		win.blit(bg,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		
		win.blit(shopic,(175,290))
		win.blit(invenic,(780,350))
		win.blit(shop_text,(275,200))
		win.blit(inventory_text,(800,200))
		win.blit(arrow,(0,0))
		char.updatehand(win)

		mouse = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()
		
		if mouse_press[0] == 1:
			if 50 > mouse[0] > 0 and 50 > mouse[1] > 0:
				menu.mainmenu(win,char)
			elif 475 > mouse[0] > 175 and 590 > mouse[1] > 290:
				shop_menu(win,char)
			elif 1180 > mouse[0] > 780 and 542 > mouse[1] > 350:
				inventory(win,char)
	
	pygame.display.flip()

def shop_menu(win,char):

	#function to display shop menu

	bg = pygame.image.load('backgrounds/shop_menu.png').convert_alpha()

	clock = pygame.time.Clock()

	bg = pygame.transform.scale(bg,(1280,720))
	
	grey = (220,220,220)
	black = (0,0,0)

	font = pygame.font.SysFont('Impact',16)
	costfont = font.render('Cost: ',False,(255,255,255))

	boss_check = check_BTicket()

	b_ticket = pygame.image.load('imgs/boss_ticket.png').convert_alpha()
	b_ticket = pygame.transform.scale(b_ticket,(250,250))

	coin = pygame.image.load('imgs/coin.png').convert_alpha()
	upcoin = pygame.transform.scale(coin,(20,15))
	
	#gets the cost of each item
	dhct,fhct,phct,p5ct,sct,fbtct = pf.getcost()

	#display player gold amount
	gold_amt = pf.displaygold()

	x = [50,300,550,800,1050]
	shopping = True
	while shopping:
		clock.tick(120)
		item = ""
		win.blit(bg,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		for i in x:
			win.blit(costfont,(i+50,307))
			win.blit(upcoin,(i+125,310))
		
		if boss_check == "False":
			pygame.draw.rect(win,grey,(490,350,300,300))
			pygame.draw.rect(win,black,(490,650,300,30))
			win.blit(b_ticket,(515,375))
			win.blit(fbtct,(635,657))
			win.blit(costfont,(535,657))
			win.blit(upcoin,(610,660))

		win.blit(dhct,(200,307))
		win.blit(fhct,(450,307))
		win.blit(phct,(700,307))
		win.blit(p5ct,(950,307))
		win.blit(sct,(1200,307))
		win.blit(gold_amt,(1180,15))


		char.updatehand(win)

		pygame.display.flip()

		mouse = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()

		z = False
		if mouse_press[0] == 1:
			if 50 > mouse[0] > 0 and 50 > mouse[1] > 0:
				merchant_menu(win,char)
			elif 250 > mouse[0] > 50 and 330 > mouse[1] > 100:
				item = "Default Hand"
				z,item_cost = balcheck(win,char,item)
			elif 500 > mouse[0] > 300 and 330 > mouse[1] > 100:
				item  = "Fire Hand"
				z,item_cost = balcheck(win,char,item)
			elif 750 > mouse[0] > 550 and 330 > mouse[1] > 100:
				item = "Poison Hand"
				z,item_cost = balcheck(win,char,item)	
			elif 1000 > mouse[0] > 800 and 330 > mouse[1] > 100:
				item = "Slow"
				z,item_cost = balcheck(win,char,item)
			elif 1250 > mouse[0] > 1050 and 330 > mouse[1] > 100:
				item = "Plus 5"
				z,item_cost = balcheck(win,char,item)
			elif 790 > mouse[0] > 490 and 680 > mouse[1] > 350 and boss_check == "False":
				item = "Final Boss Ticket"
				z,item_cost = balcheck(win,char,item)
		if z:
			shopping = False
			purchase_confirm(win,char,item,item_cost)

def inventory(win,char):

	#function to display the inventory
	bg = pygame.image.load('backgrounds/merchant.jpg').convert_alpha()

	arrow = pygame.image.load('imgs/l_arrow.png').convert_alpha()
	arrow = pygame.transform.scale(arrow,(50,50))

	grey = (220,220,220)
	
	dh = pygame.image.load('hands/cursor_hand.png').convert_alpha()
	fh = pygame.image.load('hands/flame_hand.png').convert_alpha()
	ph = pygame.image.load('hands/poison_hand.png').convert_alpha()
	slow = pygame.image.load('imgs/slow.png').convert_alpha()
	timer = pygame.image.load('imgs/timer.png').convert_alpha()
	b_ticket = pygame.image.load('imgs/boss_ticket.png').convert_alpha()
	chains = pygame.image.load('imgs/locked.png').convert_alpha()

	dh = pygame.transform.scale(dh,(150,150))
	fh = pygame.transform.scale(fh,(150,150))
	ph = pygame.transform.scale(ph,(150,150))
	slow = pygame.transform.scale(slow,(150,150))
	timer = pygame.transform.scale(timer,(108,150))
	b_ticket = pygame.transform.scale(b_ticket,(150,150))
	chains = pygame.transform.scale(chains,(200,200))

	a = [400,800]
	b = [50,275,500]


	#fhu = Firehand Unlock, PHU = poisonhand unlock, p5u = plus 5 count, su = slow count, fbtu = final boss ticket unlock 
	fhu,phu,p5u,su,fbtu = check_unlocks()

	explainfont = pygame.font.SysFont('Impact',18)
	amountfont = pygame.font.SysFont('Impact',32)

	slowamt = amountfont.render(str(su),True,(0,0,0))
	p5amt = amountfont.render(str(p5u),True,(0,0,0))

	exptext1 = explainfont.render('Click on any unlocked hands to equip it.',False,(0,0,0))
	exptext2 = explainfont.render('The numbers on the bottom right',False,(0,0,0))
	exptext3 = explainfont.render('shows how many powerups you own.',False,(0,0,0))
	exptext4 = explainfont.render('To activate your powerups in hunts:',False,(0,0,0))
	exptext5 = explainfont.render('K: For the Plus 5 Power Up',False,(0,0,0))
	exptext6 = explainfont.render('L: For the Slow Power Up',False,(0,0,0))
	exptext7 = explainfont.render('Boss Space Mode Controls:',False,(0,0,0))
	exptext8 = explainfont.render('Arrow buttons for movement',False,(0,0,0))
	exptext9 = explainfont.render('Space to shoot the Mosquito Boss',False,(0,0,0))
	exptext10 = explainfont.render('5 stages',False,(0,0,0))

	

	managing = True
	while managing:
		win.blit(bg,(0,0))
		pygame.draw.rect(win,grey,(0,0,300,720))
		win.blit(exptext1,(10,80))
		win.blit(exptext2,(10,130))
		win.blit(exptext3,(10,145))
		win.blit(exptext4,(10,180))
		win.blit(exptext5,(10,210))
		win.blit(exptext6,(10,230))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		for i in a:
			for j in b:
				pygame.draw.rect(win,grey,(i,j,200,200))

		win.blit(dh,(425,75))
		
		if fhu == True:
			win.blit(fh,(425,300))
		else:
			win.blit(chains,(400,275))
		

		if phu == True:
			win.blit(ph,(425,525))
		else:
			win.blit(chains,(400,500))

		win.blit(slow,(825,75))
		win.blit(slowamt,(980,210))

		win.blit(timer,(846,300))
		win.blit(p5amt,(980,435))

		if fbtu == True:
			win.blit(b_ticket,(825,525))
			win.blit(exptext7,(10,320))
			win.blit(exptext8,(10,360))
			win.blit(exptext9,(10,380))
			win.blit(exptext9,(10,400))
		else:
			win.blit(chains,(800,500))

		win.blit(arrow,(0,0))
		char.updatehand(win)
		pygame.display.update()

		mouse_press = pygame.mouse.get_pressed()
		mouse = pygame.mouse.get_pos()

		if mouse_press[0] == 1:
			if 50 > mouse[0] > 0 and 50 > mouse[1] > 0:
				menu.mainmenu(win,char)
			elif 600 > mouse[0] > 400 and 250 > mouse[1] > 50:
				hand = "DH"
				#changes the equipped hand
				char.changehand(hand)
				#gets the current equipped, so the hand can be "recreated"
				equipped = pf.cur_cursor()
				char = Hand(equipped)
			elif 600 > mouse[0] > 400 and 475 > mouse[1] > 275 and fhu == True:
				hand = "FH"
				char.changehand(hand)
				equipped = pf.cur_cursor()
				char = Hand(equipped)
			elif 600 > mouse[0] > 400 and 700 > mouse[1] > 500 and phu == True:
				hand = "PH"
				char.changehand(hand)
				equipped = pf.cur_cursor()
				char = Hand(equipped)


def balcheck(win,char,item):

	#function to check if the player has enough gold to purchase the clicked item
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]

	denied = pygame.mixer.Sound('sounds/not_enough.wav')
	for j in y:
		for i in range(int(len(j)+1)):
			if j[i] == "Balance":
				bal = int(j[i+1])
			elif j[i] == item:
				item_cost = int(j[i+2])
				break
	if bal >= item_cost:
		return True,item_cost
	elif bal < item_cost:
		denied.play()
		return False,item_cost
		

def purchase_confirm(win,char,item,item_cost):

	#function to display the purchase confirmation screen
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]

	red = (175,0,0)
	green =(34,139,34)
	bright_red = (255,0,0)
	bright_green = (0,255,0)
	gold = (255,215,0)

	font = pygame.font.SysFont('Impact', 64)
	
	purchtext = font.render('Purchase?',True,red)	
	
	itemtext = font.render(str(item) + '  for  ' + str(item_cost) + '  Gold  ',False,gold)
	
	confirmed = False
	
	#displays the power increase
	if item == "Default Hand":
		h_pow,next_pow = char.upgradeDH(confirmed)
		pow_text = font.render('Power will increased from  ' + str(h_pow) +'  to  ' + str(next_pow), False, red)
	elif item == "Fire Hand":
		h_pow,next_pow = char.upgradeFH(confirmed)
		pow_text = font.render('Power will increased from  ' + str(h_pow) +'  to  ' + str(next_pow), False, red)
	elif item == "Poison Hand":
		h_pow,next_pow = char.upgradePH(confirmed)
		pow_text = font.render('Power will increased from  ' + str(h_pow) +'  to  ' + str(next_pow), False, red)
	else:
		pow_text = font.render('', False, (0,0,0))

	optionFont = pygame.font.SysFont('Impact', 26)
	confirm = optionFont.render('Confirm',False,(0,0,0))
	cancel = optionFont.render('Cancel',False,(0,0,0))

	purchasing = True

	while purchasing:

		#blits the purchasing confirmation text
		win.fill((255,255,255))
		win.blit(purchtext,(500,50))
		win.blit(itemtext,(300,150))
		win.blit(pow_text,(200,350))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		mouse = pygame.mouse.get_pos()
		
		#box changes according to the cursor position
		if 400+200 > mouse[0] > 400 -char.width+5 and 600+75 > mouse[1] > 600-char.height:
			pygame.draw.rect(win, bright_green,(400,600,200,75))
		else:
			pygame.draw.rect(win, green,(400,600,200,75))

		if 800 + 200 > mouse[0] > 800 -char.width+5 and 600 + 75 > mouse[1] > 600-char.height:
			pygame.draw.rect(win, bright_red,(800,600,200,75))
		else:
			pygame.draw.rect(win, red,(800,600,200,75))

		win.blit(confirm,(450,630))
		win.blit(cancel,(850,630))
		char.updatehand(win)
		pygame.display.flip()
		
		mouse = pygame.mouse.get_pos()
		mouse1 = pygame.mouse.get_pressed()
		
		#checks if the player chose confirm or cancel
		if mouse1[0] == 1 and 800 + 200 > mouse[0] > 800 -char.width + 5 and 600 + 75 > mouse[1] > 600-char.height:
			purchasing = False
			shop_menu(win,char)
		elif mouse1[0] == 1 and 400+200 > mouse[0] > 400 -char.width + 5 and 600+75 > mouse[1] > 600-char.height:
			ching = pygame.mixer.Sound('sounds/purchased!.wav')
			ching.play()
			purchase(win,char,item,item_cost)
			purhasing = False
	data.close()

def purchase(win,char,item,item_cost):

	#function to change the data in the text file for purchases
	confirmed = True
	#upgrades hand power
	if item == "Default Hand":
		char.upgradeDH(confirmed)
	elif item == "Fire Hand":
		char.upgradeFH(confirmed)
	elif item == "Poison Hand":
		char.upgradePH(confirmed)
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]
	
	del y[0][-1]
	
	if item == "Plus 5" or item == "Slow":
		for j in y:
			for i in range(int(len(j)+1)):
				if j[i] == item:
					j[i+1] = int(j[i+1]) + 1
					break

	elif item == "Final Boss Ticket":
		for j in y:
			for i in range(int(len(j)+1)):
				if j[i] == item:
					j[i+1] = True
					break

	for j in y:
		for i in range(int(len(j)+1)):
			if j[i] == "Balance":
				j[i+1] = int(j[i+1]) - int(item_cost)
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

	shop_menu(win,char)

def check_BTicket():

	#checks if the player already has a boss ticket
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]

	for j in y:
		for i in range(int(len(j)+1)):
			if j[i] == "Final Boss Ticket":
				return j[i+1]

def check_unlocks():

	#checks whatever the player has unlocked for the inventory
	data = open("SaveData.txt","r+")
	y = [line.split(',') for line in data.readlines()]

	for j in y:
		for i in range(int(len(j)+1)):
			if j[i] == "Fire Hand":
				if j[i+1] == '0':
					fhu = False
				else:
					fhu = True
			elif j[i] == "Poison Hand":
				if j[i+1] == '0':
					phu = False
				else:
					phu = True
			elif j[i] == "Plus 5":
				p5u = str(j[i+1])

			elif j[i] == "Slow":
				su = str(j[i+1])

			elif j[i] == "Final Boss Ticket":
				if j[i+1] == "False":
					fbtu = False
					break
				else:
					fbtu = True
					break
	#returns True or False for each unlock
	return fhu,phu,p5u,su,fbtu


