import pygame
import sys
import time
import os
import math


import menus as menu
import playerfunctions as pf
import boss_fight as bf

from mosquito import Mosquito



def updateHuntDisplay(bg,win,pos,char,time_rmn,flames,fumes,curr_hand):

    #function to update all the images on the screen
    
    heart = pygame.image.load('imgs/heart.png').convert_alpha()

    heart = pygame.transform.scale(heart,(48,48))

    time_font = pygame.font.SysFont('Impact',64)
    hp_font = pygame.font.SysFont('Impact',40)
    
    time_rmn = round(time_rmn,0)
    
    hp = hp_font.render(str(pos.health),False,(255,0,0))
    time_left = time_font.render(str(time_rmn),False,(255,255,255))

    win.fill((0,0,0))
    win.blit(bg,(0,0))

    
    if curr_hand == "FH":
        flames = pos.flamehitcheck(flames)
        flames = updateflames(win,flames)

    elif curr_hand == "PH":
        pos.poisonhitcheck(fumes)
        expandfumes(win,fumes)
    

    
    win.blit(heart,(12,12))
    win.blit(hp,(70,12))
    win.blit(time_left,(575,12))
    win.blit(pos.image,(pos.x,pos.y))
    char.updatehand(win)
    pygame.display.flip()


def mosquitohunt(win,char,stage):

    bg = pygame.image.load('backgrounds/bg.jpg').convert_alpha()

    #function for the mosquito hunt battle mode

    pygame.mixer.music.stop()

    pygame.mixer.music.load('sounds/hunt_theme.mp3')
    pygame.mixer.music.play(-1)
    
    flame_sound = pygame.mixer.Sound('sounds/flame_place.wav')
    poison_sound = pygame.mixer.Sound('sounds/poison_gas.wav')

    h_pow = char.mypow()
    pos = Mosquito(stage)

    curr_hand = char.equipping()

    time_lim = 15
    
    flames = []
    fumes = []

    run = True
    start = time.time()
    clock = pygame.time.Clock()
    newflame = 0
    last_move = 0

    bbg = False
    while run == True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    powerup = "Plus 5"
                    use = poweruse(powerup)
                    if use:
                        time_lim += 5
                elif event.key == pygame.K_l:
                    powerup = "Slow"
                    use = poweruse(powerup);
                    if use:
                        pos.vel = int(pos.vel/2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos.hitcheck(h_pow)

                elif event.button == 3:
                    if curr_hand == "FH" and time.time() - newflame > 0.5:
                        flames = flamecreate(flames,flame_sound)
                        newflame = time.time()

                    elif curr_hand == "PH":
                        create_fume(fumes,poison_sound)

        death = pos.killcheck()
        if death == True:
            pygame.mixer.music.stop()
            mosqplostion(bg,win,char,pos,bbg)
            menu.winmenu(win,pos.gold,char)

        if time.time() - last_move >= 0.15:
            pos.movement()
            last_move = time.time()

        elapsed = time.time() - start
        time_rmn = time_lim - elapsed
        if elapsed >= time_lim:
            run = False
            menu.losemenu(win,char)

        updateHuntDisplay(bg,win,pos,char,time_rmn,flames,fumes,curr_hand)
    

def poweruse(powerup):

    #function to check for powerup uses

    data = open("SaveData.txt","r+")
    y = [line.split(',') for line in data.readlines()]
    del y[0][-1]

    for j in y:
        for i in range(int(len(j)+1)):
            if j[i] == powerup:
                if int(j[i+1]) >= 1:
                    j[i+1] = int(j[i+1]) - 1
                    data.seek(0)
                    data.truncate()
                    for j in y:
                        for i in j:
                            data.write(str(i)+',')
                    data.flush()
                    os.fsync(data.fileno())
                    data.close()
                    return True
                elif int(j[i+1]) <= 0:
                    return False

def flamecreate(flames,flame_sound):   

    #function to create flames on right click with flame
    
    if 0 <= len(flames) < 6:
        flame_sound.play()
        m_pos = pygame.mouse.get_pos()
        flames.append(m_pos[0])
        flames.append(m_pos[1])
        flames.append(time.time())
    #deletes any extra flames, only 2 flames on the screen at one time
    elif len(flames) > 6:
        flames = flames[:6]
    return flames

def updateflames(win,flames):

    #function to update flames
    curr = time.time()

    hot = pygame.image.load('imgs/fire.png').convert_alpha()
    hot = pygame.transform.scale(hot,(70,70))

    if len(flames) == 3:
        if curr - flames[-1] >= 5:
            del flames[:]
        else:
            win.blit(hot,(flames[0],flames[1]))
    elif len(flames) == 6: 
        if curr - flames[2] >= 5 and curr - flames[-1] >= 5:
            del flames[:]
        elif curr - flames[2] >= 5:
            flames = flames[3:]
            win.blit(hot,(flames[0],flames[1]))
        elif curr - flames[-1] >= 5:
            flames = flames[:3]
            win.blit(hot,(flames[0],flames[1]))
        else:
            win.blit(hot,(flames[0],flames[1]))
            win.blit(hot,(flames[3],flames[4]))
    return flames


def create_fume(fumes,fumes_sound):

    #funtion to create the green poison cloud/fumes
    if 0 <= len(fumes) < 4:
        m_pos = pygame.mouse.get_pos()
        fumes.append(m_pos[0])
        fumes.append(m_pos[1])
        fumes.append(time.time())
        fumes.append(2)
        fumes_sound.play()
    #deletes additional fumes, only 1 at once
    elif len(fumes) > 4:
        fumes = fumes[:4]

def expandfumes(win,fumes):

    #function to expand the fume poison cloud

    dark_green = (11,102,35)
    
    curr = time.time()

    if len(fumes) > 0:

        pygame.draw.circle(win,dark_green,(fumes[0],fumes[1]),fumes[3])

        fumes[3] = fumes[3] + 3
            
        #if the fumes has been on screen for more than 9 seconds, delete the fume

        if curr - fumes[2] >= 9:
            del fumes[:]

        
def boss_level(win,char,stage):

    bg = pygame.image.load('backgrounds/start.png').convert_alpha()

    #function for the boss level mosquito hunt mode
    
    #checks handpower
    h_pow = char.mypow()

    #creates the mosquito
    pos = Mosquito(stage*2)

    flame_sound = pygame.mixer.Sound('sounds/flame_place.wav')
    poison_sound = pygame.mixer.Sound('sounds/poison_gas.wav')
    #gets the current hand equipped
    curr_hand = char.equipping()

    time_lim = 15
    
    flames = []
    fumes = []

    run = True
    start = time.time()
    clock = pygame.time.Clock()
    newflame = 0
    last_move = 0

    bbg = False

    while run == True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

            elif event.type == pygame.KEYDOWN:
                #detection for key presses for powerup uses
                if event.key == pygame.K_k:
                    powerup = "Plus 5"
                    use = poweruse(powerup)
                    if use:
                        time_lim += 5
                elif event.key == pygame.K_l:
                    powerup = "Slow"
                    use = poweruse(powerup);
                    if use:
                        pos.vel = int(pos.vel/2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #checks if mosquito is hit
                    pos.hitcheck(h_pow)


                elif event.button == 3:

                    if curr_hand == "FH" and time.time() - newflame > 0.5:
                        #only works with flame hand
                        #creates flames if gap between last one created is >= 0.5 seconds
                        flames = flamecreate(flames,flame_sound)
                        newflame = time.time()

                    elif curr_hand == "PH":
                        #only works with poison hand
                        #creates a fume
                        create_fume(fumes,poison_sound)

        #checks if the mosquito has died
        death = pos.killcheck()
        if death == True:
            mosqplostion(bg,win,char,pos,bbg)
            bf.main(win,char,stage)
            break
        if time.time() - last_move >= 0.15:
            pos.movement()
            last_move = time.time()


        #checks if the timer has passed
        elapsed = time.time() - start
        time_rmn = time_lim - elapsed
        if elapsed >= time_lim:
            run = False
            menu.losemenu(win,char)
            break
    
        updateHuntDisplay(bg,win,pos,char,time_rmn,flames,fumes,curr_hand)

def mosqplostion(bg,win,char,pos,bbg):


    #function for the animation for the mosquito explosion
    #bbg is boss background, it is only True during the ship battle mode 


    explosion = pygame.mixer.Sound('sounds/explosion.wav')

    bg = pygame.transform.scale(bg,(1280,720))

    frames = [pygame.image.load('explode_anim/frame0.gif'),pygame.image.load('explode_anim/frame1.gif'),pygame.image.load('explode_anim/frame2.gif'),
              pygame.image.load('explode_anim/frame3.gif'),pygame.image.load('explode_anim/frame4.gif'),pygame.image.load('explode_anim/frame5.gif'),
              pygame.image.load('explode_anim/frame6.gif'),pygame.image.load('explode_anim/frame7.gif'),pygame.image.load('explode_anim/frame8.gif'),
              pygame.image.load('explode_anim/frame9.gif'),pygame.image.load('explode_anim/frame10.gif'),pygame.image.load('explode_anim/frame11.gif')]
    explosion.play()
    for frame in frames:
        win.blit(bg,(0,0))
        if bbg == False:
            win.blit(frame,(pos.x-150,pos.y-150))
        elif bbg == True:
            win.blit(frame,(pos.hitbox[0]-150,pos.hitbox[1]-150))
        time.sleep(0.1)
        char.updatehand(win)
        pygame.display.update()

