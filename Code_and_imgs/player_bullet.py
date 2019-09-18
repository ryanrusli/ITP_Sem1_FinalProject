import pygame

class Bullet:
    def __init__(self,charx,chary,color):
        #player bullet attributes
        self.x = charx
        self.y = chary
        self.radius = 8
        self.color = color
        self.vel = 20 
        self.limit = 10

    def draw(self,win):
        #draws a new player bullet onto the screen
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

    def update(self,bullets,win,the_boss):

        for bullet in bullets:
            #checks if the bullet collides with the alien hitbox
            if bullet.y - bullet.radius < the_boss.hitbox[1] + the_boss.hitbox[3] and bullet.y + bullet.radius > the_boss.hitbox[1]:
                if bullet.x + bullet.radius > the_boss.hitbox[0] and bullet.x - bullet.radius < the_boss.hitbox[0] + the_boss.hitbox[2]:
                    bullets.pop(bullets.index(bullet))
                    the_boss.hit()            

            #moves the bullet upwards if its still within the screen
            if bullet.y < 1280 and bullet.y > 0:
                bullet.y -= bullet.vel
            else:
                #removes the bullet if it collides with the top of the screen
                bullets.pop(bullets.index(bullet)) 
            bullet.draw(win)
        
    


