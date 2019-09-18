import pygame

class Ship:
    def __init__(self):

        #player ship attributes for the final boss
        self.image = pygame.image.load('characters/epoch.png')
        self.width = 114
        self.height = 64
        self.ship = pygame.transform.scale(self.image,(self.width,self.height))
        
        self.x = 640
        self.y = 650
        self.vel = 20
        
        #ship hitbox
        self.hitbox = (self.x+20,self.y+20,self.width-30,self.height-30)

        self.lives = 4


    def blitme(self,win):
        #updates the ship position and image
        win.blit(self.ship,(self.x,self.y))
        self.hitbox = (self.x+20,self.y+20,self.width-30,self.height-30)
       
        pygame.font.init()

        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        Lives = myfont.render('Player Health:'+ str(self.lives), False, (255, 255, 255))

        win.blit(Lives,(0,0))



    def shiphit(self):
        #reduces ship health
        self.lives -= 1

    def lifecheck(self):

        #checks if the ship health is already less than 0
        if self.lives <= 0:
            return True
        else:
            return False


            

