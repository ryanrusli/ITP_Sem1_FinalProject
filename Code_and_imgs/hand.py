import pygame
import os
import sys
import shopfunctions as sf

class Hand:

    def __init__(self,equipped):    
        #Hand attributes
        self.width = 48
        self.height = 48
        if equipped == "DH":
            self.image = pygame.image.load('hands/cursor_hand.png').convert_alpha()
        elif equipped == "FH":
            self.image = pygame.image.load('hands/flame_hand.png').convert_alpha()
        elif equipped == "PH":
            self.image = pygame.image.load('hands/poison_hand.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.equipped = equipped
    
    def updatehand(self,win):
        #function to update the custom cursor to the proper position
        pygame.mouse.set_visible(False)
        mouse = pygame.mouse.get_pos()
        xpos = mouse[0]
        ypos = mouse[1]
        win.blit(self.image,(xpos,ypos))
        pygame.display.update()

    def changehand(self,new_hand):

        #function if the user changes the equipped hand
        data = open("SaveData.txt","r+")
        y = [line.split(',') for line in data.readlines()]

        for j in y:
            for i in range(int(len(j)+1)):
                if j[i] == "Equipped":
                    j[i+1] = str(new_hand)
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


    def equipping(self):
        #returns equipped hand
        return self.equipped


    def mypow(self):

        #gets the strength for the current hand being used
        using = ''
        data = open("SaveData.txt","r+")
        y = [line.split(',') for line in data.readlines()]
        if self.equipped == "DH":
            using = "Default Hand"
        elif self.equipped == "FH":
            using = "Fire Hand"
        elif self.equipped == "PH":
            using = "Poison Hand"
        for j in y:
            for i in range(int(len(j))+1):
                if j[i] == using:
                    h_pow = int(y[0][i+1]) 
                    break
        #returns the hand power
        return h_pow

    
    def upgradeDH(self,confirmed):

        #function for a default hand upgrade
        data = open("SaveData.txt","r+")
        y = [line.split(',') for line in data.readlines()]
        del y[0][-1]
        for j in y:
            for i in range(int(len(j))+1):
                if j[i] == "Default Hand":
                    h_pow = int(j[i+1])
                    next_pow = h_pow + 1 
                    if confirmed == True:

                        #increases the cost and power
                        j[i+1] = next_pow
                        j[i+2] = int(j[i+2]) + 8

                        #rewrites the data
                        data.seek(0)
                        data.truncate()
                        for j in y:
                            for i in j:
                                data.write(str(i)+',')
                        data.flush()
                        os.fsync(data.fileno())
                        data.close()
                    break
        return h_pow,next_pow


    def upgradeFH(self,confirmed):

        #function for a fire hand upgrade
        data = open("SaveData.txt","r+")
        y = [line.split(',') for line in data.readlines()]
        del y[0][-1]
        for j in y:
            for i in range(int(len(j))+1):
                if j[i] == "Fire Hand":
                    h_pow = int(j[i+1]) 
                    next_pow = h_pow + 2
                    if confirmed:
                        #increases the cost and power
                        j[i+1] = next_pow
                        j[i+2] = int(j[i+2]) + 20
                        
                        #rewrites the data
                        data.seek(0)
                        data.truncate()
                        for j in y:
                            for i in j:
                                data.write(str(i)+',')

                        data.flush()
                        os.fsync(data.fileno())
                        data.close()
                    break
        return h_pow,next_pow
    
    def upgradePH(self,confirmed):

        #function for a poison hand upgrade
        data = open("SaveData.txt","r+")
        y = [line.split(',') for line in data.readlines()]
        del y[0][-1]
        for j in y:
            for i in range(int(len(j))+1):
                if j[i] == "Poison Hand":
                    h_pow = int(j[i+1]) 
                    next_pow = h_pow + 2
                    if confirmed:
                        #increases the cost and power
                        j[i+1] = next_pow
                        j[i+2] = int(j[i+2]) + 30

                        #rewrites the data
                        data.seek(0)
                        data.truncate()
                        for j in y:
                            for i in j:
                                data.write(str(i)+',')

                        data.flush()
                        os.fsync(data.fileno())
                        data.close()
                    break
        return h_pow,next_pow

