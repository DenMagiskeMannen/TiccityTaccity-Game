# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:11:22 2024

@author: teodo
"""

#TictacSuperToe
import pygame
import time


#Ideer;
#Øyne med farger, turns, «Win», selection understanding, øyne åpne lukke animasjoner, plasering av brikke animasjon, tenker en liten surge med farge som roer seg ned til tegnet., øynene er «Tilskuere» som er for mektige for dimensjonen, så det blir mer og mer ekkelt med hver brikke plassert, når ene har vunnet så kommer alle andre «Tilskuere» inn å gjør en stille applaus, noe som ødelegger dimensjonen med et «CRACK», du spiller som en av fargene som dukket opp for å gi deg applaus., PvE og PvP, der PvE vil det stå noe slik som, «Voyage the void» eller «Tackle the abyss» eller «Deny the destruction»., mens PvP vil være «Challange your challanger»
#TODO
#Gjør at tictacså er arrangert fra høyest til lavest size
#Iterer gjennom dem for å sjekke hvilken sin main hitbox de er inni, fra start til slutt

screenie=(1280, 720)


pygame.init()
screen = pygame.display.set_mode(screenie)
clock = pygame.time.Clock()
running = True
dt = 0


games=[]

class TicTac:
    Taccies=[]
    Game_state=0
    Player_alternatives=["O","X"]
    Current_player=Player_alternatives[0]
    def __init__(self,x,y,size,lines=3,thickness=2):
        self.winner=None
        self.thickness=thickness
        #self.super_subsidery=subsidery_target
        #subsidery_target=None
        self.amount=size*2/lines
        #self.subsidery_areal=int(self.amount*2)
        self.subsidery_middle=int(self.amount/2)
        self.points=[]
        self.Start_X=x
        self.Start_Y=y
        self.Y_conditions=[y-size,y+size]
        self.X_conditions=[x-size,x+size]
        
        for i in range(1,lines):
            line=[(self.X_conditions[0],int(self.Y_conditions[0]+self.amount*i)),(self.X_conditions[1],int(self.Y_conditions[0]+self.amount*i))]
            self.points.append(line)
        for i in range(1,lines):
            line=[(int(self.X_conditions[0]+self.amount*i),self.Y_conditions[0]),(int(self.X_conditions[0]+self.amount*i),self.Y_conditions[1])]
            self.points.append(line)
        self.lines=lines
        self.hitboxes=[]
        self.game_status=[]
        #Makes Individual hitboxes for the boxes?
        for x in range(lines):
            for y in range(lines):
                #Need min x, max x
                #And min y, max y 
                minX= self.X_conditions[0]+x*self.amount
                maxX= self.X_conditions[0]+(x+1)*self.amount
                X_hitbox=[minX,maxX]
                
                minY= self.Y_conditions[0]+y*self.amount
                maxY= self.Y_conditions[0]+(y+1)*self.amount
                Y_hitbox=[minY,maxY]
                self.hitboxes.append([X_hitbox,Y_hitbox])
                self.game_status.append(["_",X_hitbox[0]+self.subsidery_middle,Y_hitbox[0]+self.subsidery_middle])
        self.Taccies.append(self)
        
    def reset(self):
        for sign in self.game_status:
            sign[0]="_"
        self.winner=None
    
    def handle_click(self,x,y):
        
        for index, hitbox in enumerate(self.hitboxes):
            check=[False,False]
            if hitbox[0][0] < x and hitbox[0][1] > x:
                check[0]=True
            if hitbox[1][0] < y and hitbox[1][1] > y:
                check[1]=True
            if check[0] == True and check[1] == True and self.game_status[index][0]=="_":
                self.game_status[index][0]=self.Current_player
                TicTac.switch_turn(TicTac)

    def check_winner(self):
        self.Vicotry_options=[]
        
        #Comoulms
        ColoumnLength=self.lines
        for i in range(self.lines):
            ColoumnIndex=i*self.lines
            Row=[]
            for j in range(ColoumnLength):
                Row.append(self.game_status[ColoumnIndex+j][0])
            self.Vicotry_options.append(Row)
                
        #layers
        for i in range(self.lines):
            LayerIndex=i
            Row=[]
            for j in range(self.lines):
                LayerOperation=j*self.lines
                Row.append(self.game_status[LayerIndex+LayerOperation][0])
            self.Vicotry_options.append(Row)
        
        #Diagonals
        Row=[]
        for i in range(self.lines):
            index=i*(self.lines+1)
            Row.append(self.game_status[index][0])
        self.Vicotry_options.append(Row)
        
        Row=[]
        for i in range(self.lines):
            #2 tilbake, så 3 tilbake
            index=((self.lines-1)+i*(self.lines-1))
            Row.append(self.game_status[index][0])
        self.Vicotry_options.append(Row)
        
        for option in self.Vicotry_options:
            if all(element == self.Player_alternatives[0] for element in option):
                self.winner="O"
            if all(element == self.Player_alternatives[1] for element in option):
                self.winner="X"
    
    def Cheat_win(self,Overpower=False):
        if Overpower== True:
            for tile in self.game_status:
                tile[0]=self.Current_player
        else:
            for tile in self.game_status:
                if tile[0]=="_":
                    tile[0]=self.Current_player
    
    def draw_base(self):
        for line in self.points:
            pygame.draw.line(screen,"white",line[0],line[1],self.thickness)
        
        for sign in self.game_status:
            if sign[0]=="X":
                self.draw_X(sign[1],sign[2],self.amount/3)
            if sign[0]=="O":
                self.draw_O(sign[1],sign[2],self.amount/3)
        
        if self.winner != None:
            if self.winner=="O":
                self.draw_O(self.Start_X, self.Start_Y, self.amount*2)
            else:
                self.draw_X(self.Start_X, self.Start_Y, self.amount*2)
    def draw_X(self,middleX,middleY,size):
        pygame.draw.circle(screen,"red",(middleX,middleY), size)
    def draw_O(self,middleX,middleY,size):
        pygame.draw.circle(screen,"white",(middleX,middleY), size)
        
    @classmethod
    def check_hitboxes(cls, x, y):
        #Ping main, whitch pings the lil box
        Main_Tac=None
        for Tac in cls.Taccies:
            IN_X=False
            IN_Y=False
            if Tac.X_conditions[0]<x and Tac.X_conditions[1] > x:
                IN_X=True
            if Tac.Y_conditions[0]<y and Tac.Y_conditions[1] > y:
                IN_Y=True
            
            if IN_X == True and IN_Y == True:
                Main_Tac=Tac
                Main_Tac.handle_click(x,y)
                break
    
    def switch_turn(cls):
        cls.Game_state+=1
        if cls.Game_state % 2 != 0:
            cls.Current_player=cls.Player_alternatives[1]
        else:
            cls.Current_player=cls.Player_alternatives[0]


class SuperTicTac(TicTac):
    Superlets=[]
    def __init__(self,x,y,size,Layers=1,lines=3,thickness=5):
        super().__init__(x, y,size,lines,thickness)
        TicTac.Taccies.remove(self)
        self.Superlets.append(self)
        for game in self.game_status:
            TicTac(game[1], game[2], self.amount/2.5)

    def draw_base(self):
        for line in self.points:
            pygame.draw.line(screen,"white",line[0],line[1],self.thickness)

class Eye:
    Channels=[]
    
    def __init__(self,x,y,size,colour):
        self.x=x
        self.y=y
        self.colour=colour
        self.size=size
        self.Channels.append(self)
        
    def draw_self(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.size)



SuperTicTac(screenie[0]//2,screenie[1]//2,300)
bob=Eye(100,100,50,"white")

while running:
    current_time=time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                TicTac.check_hitboxes(event.pos[0],event.pos[1])

    screen.fill("black")
    
    Gamer=TicTac.Current_player
    """
    if Gamer =="X":
        for Channel in Eye.Channels:
            Channel.colour="red"
    elif Gamer =="O":
        for Channel in Eye.Channels:
            Channel.colour="White"
            
    """
    #Hitbox checks
    for TiccityTac in TicTac.Taccies:
        TiccityTac.draw_base()
        TiccityTac.check_winner()
    for Superduper in SuperTicTac.Superlets:
        Superduper.draw_base()
        #print(Superduper.game_status)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        for TiccityTac in TicTac.Taccies:
            TiccityTac.reset()
    if keys[pygame.K_w]:
        for TiccityTac in TicTac.Taccies:
            TiccityTac.Cheat_win()
        #TicTac.switch_turn(TicTac)
    
    for Channel in Eye.Channels:
        Channel.draw_self()
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
