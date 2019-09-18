import pygame
import sys
import time

import huntfunctions as hf
import playerfunctions as pf
import shopfunctions as sf

def startmenu(win,char):
    pygame.mixer.music.stop()

    #function for the start menu

    titlenar = pygame.mixer.Sound('sounds/genult.wav')
    titlenar.play()
    start = pygame.image.load('backgrounds/start.png').convert_alpha()

    start = pygame.transform.scale(start,(1280,720))
    win.fill((0,0,0))
    win.blit(start,(0,0))

    pygame.display.flip()

    string = ''
    text1 = ''
    text2 = ''
    imp = pygame.font.SysFont('Impact',64)

    # top_title and bot_title are for the text "animation" at the beggining

    top_title = ['M','o','s','q','u','i','t','o','   ','H','u','n','t','e','r']
    bot_title = ['G','e','n','e','r','a','t','i','o','n','s','   ','U','l','t','i','m','a','t','e']
    
    for i in top_title:
        string += i
        title = imp.render(string,False,(255,255,255))
        win.blit(title,(20,20))
        pygame.display.update()
        time.sleep(0.03)
    text1 = string
    string = ''
    time.sleep(0.4)
    for i in bot_title:
        string += i
        title = imp.render(string,False,(255,255,255))
        win.blit(title,(660,20))
        pygame.display.update()
        time.sleep(0.07)
    time.sleep(1)
    text2 = string

    pygame.mixer.music.load('sounds/startmenu.mp3')
    pygame.mixer.music.play(-1)
    
    red = (175,0,0)
    green =(34,139,34)
    bright_red = (255,0,0)
    bright_green = (0,255,0)  
    
    startmenu = True
    while startmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        win.fill((0,0,0))
        win.blit(start,(0,0))

        mouse = pygame.mouse.get_pos()

        #color of the box will change if the mouse cursor is within the box

        if 600+200 > mouse[0] > 600 -char.width+5 and 600+75 > mouse[1] > 600-char.height:
            pygame.draw.rect(win, bright_green,(600,600,200,75))
        else:
            pygame.draw.rect(win, green,(600,600,200,75))

        if 950 + 200 > mouse[0] > 950 -char.width+5 and 600 + 75 > mouse[1] > 600-char.height:
            pygame.draw.rect(win, bright_red,(950,600,200,75))
        else:
            pygame.draw.rect(win, red,(950,600,200,75))

        mouse1 = pygame.mouse.get_pressed()
        if mouse1[0] == 1 and 950 + 200 > mouse[0] > 950 -char.width + 5 and 600 + 75 > mouse[1] > 600-char.height:
            pygame.quit()
            sys.exit()
        elif mouse1[0] == 1 and 600+200 > mouse[0] > 600 -char.width + 5 and 600+75 > mouse[1] > 600-char.height:
            pygame.mixer.music.stop()
            start_sound = pygame.mixer.Sound('sounds/startbutton.wav') 
            start_sound.play()
            time.sleep(2.5)    
            transition(win)
            entry = pygame.mixer.Sound('sounds/entry.wav')   
            entry.play()
            startmenu = False
            pygame.mixer.music.load('sounds/main_menu.mp3')
            pygame.mixer.music.play(-1)
            mainmenu(win,char)

            break

        myfont = pygame.font.SysFont('Constantia',30)

        starttext = myfont.render('Start', False, (0,0,0))
        endtext = myfont.render('Quit', False, (0,0,0))

        win.blit(starttext,(665,622))
        win.blit(endtext,(1015,622))

        t1 = imp.render(text1,False,(255,255,255))
        t2 = imp.render(text2,False,(255,255,255))

        win.blit(t1,(20,20))
        win.blit(t2,(660,20))
        
        char.updatehand(win)


        pygame.display.flip()

def losemenu(win,char):

    #funtion to display the lose menu
    pygame.mixer.music.stop()
    
    win.fill((255,255,255))
    lose_sound = pygame.mixer.Sound('sounds/game_over.wav')
    loseimage = pygame.image.load('backgrounds/losemenu.jpg').convert_alpha()

    pf.losegold()

    win.blit(loseimage,(350,150))
    lose_sound.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.flip()
    time.sleep(5)
    pygame.mixer.music.load('sounds/main_menu.mp3')
    pygame.mixer.music.play(-1)

def winmenu(win,gold,char):

    #function to display the win menu
    
    win.fill((255,255,255))

    pygame.mixer.music.stop()

    pygame.mixer.music.load('sounds/win_song.mp3')
    pygame.mixer.music.play(-1)
    
    congrats = pygame.font.SysFont('Impact',64)
    goldfont = pygame.font.SysFont('Constantia',32)
    cont_text = pygame.font.SysFont('Impact',32)

    wintext = congrats.render('Congratulations!',False,(0,0,0))
    goldtext = goldfont.render('You have earned ' + str(gold) + ' gold!',False,(0,0,0))
    cont = cont_text.render('Press any key to continue...',False,(0,0,0))
    
    reward = pygame.mixer.Sound('sounds/reward.wav')


    win.blit(wintext,(400,300))
    reward.play()
    pygame.display.update()
    time.sleep(1)

    win.blit(goldtext,(450,500))
    pygame.display.update()
    reward.play()
    time.sleep(3)

    pf.gaingold(gold)
    winmenu = True
    while winmenu:
        win.fill((255,255,255))
        win.blit(cont,(450,600))
        win.blit(wintext,(400,300))
        win.blit(goldtext,(450,500))
        char.updatehand(win)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                winmenu = False
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/main_menu.mp3')
                pygame.mixer.music.play(-1)
                mainmenu(win,char)


def mainmenu(win,char):

    #function to display the main menu
    boss_check = sf.check_BTicket()
    if boss_check == "False":
        tavern = pygame.image.load('backgrounds/pre_boss_tavern.png').convert_alpha()
    elif boss_check == "True":
        tavern = pygame.image.load('backgrounds/post_boss_tavern.png')

    tavern = pygame.transform.scale(tavern,(1280,720))
    
    z = True
    mainmenu = True
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = fighter_check()
                y = merchant_check() 
                if boss_check == "True":
                    z = cat_check()

                if x == False:
                    fighter_sound = pygame.mixer.Sound('sounds/to_battle.wav')
                    fighter_sound.play()
                    time.sleep(0.2)
                    mainmenu = False
                    stageselect(win,char)
                elif y == False:
                    mainmenu = False
                    sf.merchant_menu(win,char)
                elif z == False:
                    mainmenu = False 
                    boss_transit(win,char)

        win.blit(tavern,(0,0))
        char.updatehand(win)

        pygame.display.flip()



def transition(win):

    #function for the door animation into the main menu
    frames = [pygame.image.load('door_anim/frame0.gif'),pygame.image.load('door_anim/frame1.gif'),pygame.image.load('door_anim/frame2.gif'),pygame.image.load('door_anim/frame3.gif'),pygame.image.load('door_anim/frame4.gif'),pygame.image.load('door_anim/frame5.gif'),pygame.image.load('door_anim/frame6.gif'),pygame.image.load('door_anim/frame7.gif'),
             pygame.image.load('door_anim/frame8.gif'),pygame.image.load('door_anim/frame9.gif'),pygame.image.load('door_anim/frame10.gif'),pygame.image.load('door_anim/frame11.gif'),pygame.image.load('door_anim/frame12.gif'),pygame.image.load('door_anim/frame13.gif'),pygame.image.load('door_anim/frame14.gif'),pygame.image.load('door_anim/frame15.gif'),
             pygame.image.load('door_anim/frame16.gif'),pygame.image.load('door_anim/frame17.gif'),pygame.image.load('door_anim/frame18.gif'),pygame.image.load('door_anim/frame19.gif'),pygame.image.load('door_anim/frame20.gif'),pygame.image.load('door_anim/frame21.gif'),pygame.image.load('door_anim/frame22.gif'),pygame.image.load('door_anim/frame23.gif')]
    door_creak = pygame.mixer.Sound('sounds/wooden_door.wav')
    door_creak.play()
    for frame in frames:
        frame = pygame.transform.scale(frame,(1280,720))
        win.blit(frame,(0,0))
        pygame.display.flip()
        time.sleep(0.08)
    time.sleep(2)


def stageselect(win,char):

    #function to display the stage select screen
    ss = pygame.image.load('backgrounds/stage_select.jpg')
    ss = pygame.transform.scale(ss,(1280,720))

    arrow = pygame.image.load('imgs/l_arrow.png')
    arrow = pygame.transform.scale(arrow,(50,50))

    grey = (220,220,220)        

    myfont = pygame.font.SysFont('Constantia',32)

    x =[100,680]
    y =[50,190,330,470,610] 

    stages = ['Stage 1','Stage 2','Stage 3','Stage 4','Stage 5','Stage 6','Stage 7','Stage 8','Stage 9','Stage 10']
    count = 0
    stagesel = True
    while stagesel:
        win.blit(ss,(0,0))
        win.blit(arrow,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in x:
            for q in y:
                stageNo = myfont.render(stages[count],False,(0,0,0))
                pygame.draw.rect(win,grey,(i,q,500,75))
                win.blit(stageNo,(i+175,q+25))
                count += 1
        count = 0
        
        char.updatehand(win)

        mouse = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        if mouse_press[0] == 1:
            if 600 > mouse[0] > 100 and 125 > mouse[1] > 50:
                stage = 1
                hf.mosquitohunt(win,char,stage)
            elif 600 > mouse[0] > 100 and 265 > mouse[1] > 190:
                stage = 2
                hf.mosquitohunt(win,char,stage)
            elif 600 > mouse[0] > 100 and 405 > mouse[1] > 330:
                stage = 3
                hf.mosquitohunt(win,char,stage)
            elif 600 > mouse[0] > 100 and 545 > mouse[1] > 470:
                stage = 4
                hf.mosquitohunt(win,char,stage)
            elif 600 > mouse[0] > 100 and 685 > mouse[1] > 610:
                stage = 5
                hf.mosquitohunt(win,char,stage)
            elif 1180 > mouse[0] > 680 and 125 > mouse[1] > 50:
                stage = 6
                hf.mosquitohunt(win,char,stage)
            elif 1180 > mouse[0] > 680 and 265 > mouse[1] > 190:
                stage = 7
                hf.mosquitohunt(win,char,stage)
            elif 1180 > mouse[0] > 680 and 405 > mouse[1] > 330:
                stage = 8
                hf.mosquitohunt(win,char,stage)
            elif 1180 > mouse[0] > 680 and 545 > mouse[1] > 470:
                stage = 9
                hf.mosquitohunt(win,char,stage)
            elif 1180 > mouse[0] > 680 and 685 > mouse[1] > 610:
                stage = 10
                hf.mosquitohunt(win,char,stage)
            elif 50 > mouse[0] > 0 and 50 > mouse[1] > 0:
                mainmenu(win,char)

        pygame.display.flip()


def fighter_check():

    #function to check if the battle character has been clicked

    mouse = pygame.mouse.get_pos()
    if 891 + 116 > mouse[0] > 891 and 281 + 179 > mouse[1] > 281:
        return False

def merchant_check():

    #function to check if the merchant has been clicked
    mouse = pygame.mouse.get_pos()
    if 45 + 96 > mouse[0] > 45 and 486 + 175 > mouse[1] > 486:
        return False

def cat_check():

    #function to check if the boss cat has been clicked
    mouse = pygame.mouse.get_pos()
    if 953 + 144 > mouse[0] > 953 and 547 + 136 > mouse[1] > 547:
        pygame.mixer.music.stop()
        laugh = pygame.mixer.Sound('sounds/creep_laugh.wav')
        laugh.play()
        time.sleep(2)
        pygame.mixer.music.load('sounds/bossfight.mp3')
        pygame.mixer.music.play(-1)
        return False

def boss_transit(win,char):


    #function for the boss transition animation
    anim = [pygame.image.load('kamui_anim/kamui01.gif'),pygame.image.load('kamui_anim/kamui02.gif'),pygame.image.load('kamui_anim/kamui03.gif'),
            pygame.image.load('kamui_anim/kamui04.gif'),pygame.image.load('kamui_anim/kamui05.gif'),pygame.image.load('kamui_anim/kamui06.gif'),]
    count = 0 
    anim_count = 0
    forw = 1

    #the list will only loop through 3 times
    while count < 20:
        for frame in anim:
            frame = pygame.transform.scale(frame,(1280,720))
            win.blit(frame,(0,0))
            pygame.display.update()
            time.sleep(0.05)
            count += 1

    
    hf.boss_level(win,char,1)







