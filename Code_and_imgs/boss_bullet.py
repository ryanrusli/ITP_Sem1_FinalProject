import pygame

class Bossbullet:

    def __init__(self,bulx,buly,color):
        #alien bullet attributes
        self.color = color 
        self.bulx = bulx 
        self.buly = buly 
        self.radius = 10
        self.limit = 20
        self.vel = 30


    def draw(self,win):
        #function to draw new bullets
        pygame.draw.circle(win,self.color,(self.bulx,self.buly),self.radius)

    def updatebossbul(self,win,bossb,char):
        #checks if the bullets hit the player ship hitbox
        for abullet in bossb:
            if abullet.buly - abullet.radius < char.hitbox[1] + char.hitbox[3] and abullet.buly + abullet.radius > char.hitbox[1]:
                if abullet.bulx + abullet.radius > char.hitbox[0] and abullet.bulx - abullet.radius < char.hitbox[0] + char.hitbox[2]:
                    bossb.pop(bossb.index(abullet))
                    char.shiphit()   
            #moves the bullets downwards
            if abullet.buly > 0 and abullet.buly < 730:
                abullet.buly += self.vel
            else:
                #pops the bullet if it reaches the end of the screen
                bossb.pop(bossb.index(abullet))
            abullet.draw(win)






