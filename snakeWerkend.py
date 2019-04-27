#!/usr/bin/env python3

import time
import random
import pixelFrame
from enum import Enum

class Move(Enum):
  UP = 1
  DOWN = 2
  RIGHT = 3
  LEFT = 4

class Status(Enum):
  FREE = 0
  SNAKE = 1
  HEAD = 2
  OBST = 3
  
  def __str__(self):
    if self == Status.FREE:
      return "O"
    if self == Status.SNAKE:
      return "="
    if self ==Status.HEAD:
      return "#"
    if self ==Status.OBST:
      return "X"
    return " "

class Snake:
  def __init__(self,frame,startLengte,startPositie,kleur):  
    self.pixelLijst = []
    for x in range(startLengte):
      self.pixelLijst.append((startPositie,x))
    self.itteraties = 0
    self.frame = frame
    self.kleur = kleur

  def move(self,move,groei):
    nieuweKop = (0,0)
    oudeKop = self.pixelLijst[len(self.pixelLijst)-1]    
    if move == Move.UP:
      if oudeKop[0] == 0:
        nieuweKop = (self.frame.breedte -1,oudeKop[1])
      else:
        nieuweKop = (oudeKop[0]-1,oudeKop[1])
        
    if move == Move.DOWN:
      if oudeKop[0] == self.frame.hoogte-1:
        nieuweKop = (0,oudeKop[1])
      else:
        nieuweKop = (oudeKop[0]+1,oudeKop[1])

    if move == Move.RIGHT:
      if oudeKop[1] == self.frame.breedte-1:
        nieuweKop = (oudeKop[0],0)
      else:
        nieuweKop = (oudeKop[0],oudeKop[1]+1)
    
    if move == Move.LEFT:
      if oudeKop[1] == 0:
        nieuweKop = (oudeKop[0],self.frame.breedte -1)
      else:
        nieuweKop = (oudeKop[0],oudeKop[1]-1)

    self.pixelLijst.append(nieuweKop)
    if groei == False:
      del self.pixelLijst[0]
    #print(self.pixelLijst)
    self.show()
  
  def show(self):
    #self.frame.strip.clear_strip()
    for x in range(len(self.pixelLijst)):
      self.frame.zetKleur(self.pixelLijst[x][0],self.pixelLijst[x][1],self.kleur)
    #self.frame.strip.show()        


frame = pixelFrame.Frame(16,16)
snakes = []
time.sleep(1)

for x in range(4):
  #snakes.append(Snake(frame,random.randint(1,2),random.randint(0,0xffffff)))
  snakes.append(Snake(frame,4,x,0xff0000))

while 1:
  frame.strip.clear_strip()
  for x in range(len(snakes)):    
    beweging = random.choice(list(Move))
    snakes[x].kleur = 0xff0000    
    snakes[x].move(beweging,False)
  frame.strip.show()  
  time.sleep(float(random.randrange(1,15))/100)
  
snake.frame.strip.clear_strip_show()
print(snake)

