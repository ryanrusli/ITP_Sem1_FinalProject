import pygame
import random
import time
import math



class Mosquito:
    
    def __init__(self,stage):
        #all mosquito attributes
        self.image = pygame.image.load('characters/mosq1.png').convert_alpha()
        self.width = 64
        self.height = 64
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        
        self.x = 500
        self.y = 350
        
        self.stage = stage
        self.health = self.stage * 6

        self.vel = self.stage * 11

        self.gold_mult = random.randint(3,5)

        self.gold = math.ceil(self.stage * self.gold_mult)

    def movement(self):

        #function for the random mosquito movement
        movement = ['up','down','left','right',
                    'upleft','upright','downleft','downright','stall']
        directionN = True
        while directionN == True:
            direction = str(random.choice(movement))
            if direction == "up" and self.y  > self.vel:
                self.y -= self.vel
                directionN = False
            elif direction == "down" and self.y < 700 -self.height - self.vel:
                self.y += self.vel
                directionN = False
            elif direction == "left" and self.x > self.vel:
                self.x -= self.vel
                directionN = False
            elif direction == "right" and self.x <1280 - self.width - self.vel:
                self.x += self.vel
                directionN = False
            elif direction == "upleft" and self.x > self.vel and  self.y  > self.vel:
                self.x -= self.vel/2
                self.y -= self.vel/2
                directionN = False
            elif direction == "upright" and self.x <1280 - self.width - self.vel and self.y  > self.vel:
                self.x += self.vel/2
                self.y -= self.vel/2
                directionN = False
            elif direction == "downleft" and self.x > self.vel and self.y < 700 -self.height - self.vel:
                self.x -= self.vel/2
                self.y += self.vel/2
                directionN = False
            elif direction == "downright" and self.x <1280 - self.width - self.vel and self.y < 700 -self.height - self.vel:
                self.x += self.vel/2
                self.y += self.vel/2
                directionN = False
            elif direction == "stall":
                self.x = self.x
                self.y = self.y
                directionN = False
                time.sleep(0.05)
            else:
                directionN = True

    def killcheck(self):  
        #function to check if the mosquito have died      
        if self.health <= 0:
            return True
        else:
            return False

    def hitcheck(self,h_pow):

        #function to check if the click hit the mosquito
        smack = pygame.mixer.Sound('sounds/smack.wav')

        mouse = pygame.mouse.get_pos()
        if (self.x + self.width) > mouse[0] > self.x and (self.y + self.height) > mouse[1] > self.y:
            self.health -= h_pow
            smack.play()


    def flamehitcheck(self,flames):

        #function to check if the flame hit the mosquito

        if len(flames) == 3:
            if flames[0] + 70 > self.x > flames[0] and flames[1] + 70 > self.y > flames[1]:
                self.health -= 10
                del flames[:]
        elif len(flames) == 6:
            if (flames[0] + 70 > self.x > flames[0] and flames[1] + 70 > self.y > flames[1]) and (flames[3] + 70 > self.x > flames[3] and flames[4] + 70 > self.y > flames[4]):
                self.health -= 10
                del flames[:]
            elif flames[0] + 70 > self.x > flames[0] and flames[1] + 70 > self.y > flames[1]:
                flames = flames[3:]
                self.health -= 10
            elif flames[3] + 70 > self.x > flames[3] and flames[4] + 70 > self.y > flames[4]:
                flames = flames[:3]
                self.health -= 10
        return flames

    
    def poisonhitcheck(self,fumes):

        #function to check if the poison cloud hit the mosquito

        if len(fumes) > 0:
            distance = math.hypot(self.x - fumes[0],self.y-fumes[1])
            
            if distance <= fumes[3]:
                self.health -= 0.5



