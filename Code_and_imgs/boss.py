import pygame
import random

from boss_bullet import Bossbullet

class Boss:
    def __init__(self,stage):
        #boss attributes

        self.image = pygame.image.load('characters/final_boss.png')
        self.width = 160
        self.height = 160
        self.alien = pygame.transform.scale(self.image,(self.width,self.height))
        self.x = 580
        self.y = 150
        self.stage = stage
        self.lives = 25 * self.stage
        self.speed = 15 * self.stage
        self.count = 0
    
    def createboss(self,win):
        #funciton to create the boss and the hitbox
        win.blit(self.alien,(self.x,self.y))
        self.hitbox = (self.x+50,self.y+50,self.width-70,self.height-35)
        #pygame.draw.rect(win,(255,255,255),(self.hitbox),2)

        pygame.font.init()

        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        Health = myfont.render('Boss Health:'+ str(self.lives), False, (255,255,255))

        stage = myfont.render('Stage '+str(self.stage),False,(255,255,255))

        #blits the health and stage to the screen
        win.blit(stage,(550,0))
        win.blit(Health,(1000,0))

    def bossmove(self,the_boss,bossb):

        #moves the boss
        green = (50,205,50)

        #intitialises the boss bullet
        abullet = Bossbullet(the_boss.x,the_boss.y,green)
        
        movement = False
        while movement == False:
            z = random.randint(1,15*self.stage)
            direction = random.randint(1,2)
            if direction == 1 and self.x - z > 0  :
                self.x -= z
                movement = True
                self.count += 1
            elif direction == 2 and self.x + z < 1280-self.width:
                self.x += z
                movement = True
                self.count += 1
        if 60/self.stage <= self.count:
            #boss will shoot after a certain amount of time depending on the stage
            if len(bossb) <= abullet.limit:
                bossb.append(Bossbullet(round(the_boss.x + the_boss.width //2), round(the_boss.y + the_boss.height//2), green))
                self.count = 0


    def hit(self):
        #reduces boss health
        self.lives -= 1

    def lifecheck(self):
        #checks if the boss still has any health remaningo
        if self.lives <= 0:
            return True
        else:
            return False


