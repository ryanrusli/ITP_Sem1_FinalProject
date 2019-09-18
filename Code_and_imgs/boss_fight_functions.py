import pygame 
pygame.init()

import sys
import time
import random
import menus as menu
import huntfunctions as hf

from ship import Ship
from player_bullet import Bullet
from boss import Boss
from boss_bullet import Bossbullet

def gameloop(plane,clock,win,bullets):

    #the main loop for all player actions

    white = (255,255,255)
    black = (0,0,0)
    bullet = Bullet(plane.x,plane.y,black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #detects key presses
    keys = pygame.key.get_pressed()
    if  keys[pygame.K_RIGHT] and plane.x < 1280 - plane.width - plane.vel :
        plane.x += plane.vel
    elif keys[pygame.K_LEFT] and plane.x > plane.vel:
        plane.x -= plane.vel
    elif keys[pygame.K_UP] and plane.y > plane.vel:
        plane.y -= plane.vel
    elif keys[pygame.K_DOWN] and plane.y < 720 - plane.height - plane.vel:
        plane.y += plane.vel
    elif keys[pygame.K_SPACE]:
        if len(bullets) <= bullet.limit:
            bullets.append(Bullet(round(plane.x + plane.width //2), round(plane.y + plane.height//2), white))

 


def updategamedisp(plane,win,bullets,the_boss,alienbullets,stage,char):

    #function to update the battle mode game display
    
    black = (0,0,0)
    green = (50,205,50)
    white = (255,255,255)

    bg = pygame.image.load('backgrounds/start.png')
    bg = pygame.transform.scale(bg,(1280,720))


    win.fill(black)
    win.blit(bg,(0,0))
    plane.blitme(win)
    the_boss.createboss(win)
    
    #initialises and updates the bullets
    bullet = Bullet(plane.x,plane.y,white)
    bullet.update(bullets,win,the_boss)
    
    abullet = Bossbullet(the_boss.x,the_boss.y,green)
    abullet.updatebossbul(win,alienbullets,plane)
    
    #checks the health of bothe player and boss
    g = the_boss.lifecheck()
    a = plane.lifecheck()
    bbg = True

    # a is for the player health
    # g is for the ship health

    if g == True:
        hf.mosqplostion(bg,win,char,the_boss,bbg)
        if stage == 1:
            pygame.mixer.music.stop()
            time.sleep(1)
            victory = pygame.mixer.Sound('sounds/Game_ends.wav')
            victory.play()
            time.sleep(6)
            menu.startmenu(win,char)
        else:
            stage += 1
            hf.boss_level(win,char,stage)
        
        return False


    if a == True:
        menu.losemenu(win,char)
        return False

    pygame.display.flip()
    return True
    


