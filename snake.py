#!/usr/bin/env python3
import time
import math
import random
import pixelFrame
from enum import Enum

kleurVoedsel = 0xff0000
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
      self.pixelLijst.append((x,startPositie))
    self.frame = frame
    self.kleur = kleur
    self.voedsel = (random.randint(0,15),random.randint(0,15))
    self.voedselKleur = kleur
    self.selectedMove = Move.RIGHT
    self.speed = 1            
    self.checkGrens = False
    self.maxLengte =10
    self.groei = False
    self.krimp = False
    self.laatsteMove = Move.UP
  
      
  def move(self,move,groei,show = True,):    
    self.groei = groei
    nieuweKop = (0,0)
    oudeKop = self.pixelLijst[len(self.pixelLijst)-1]  
    #De beweging toepassen en nieuwe kop berekenen  
    if move == Move.UP : # and self.laatsteMove != Move.DOWN:
      if oudeKop[0] == 0:
        if self.checkGrens:
          nieuweKop = oudeKop
        else:
          nieuweKop = (self.frame.breedte -1,oudeKop[1])          
      else:
        nieuweKop = (oudeKop[0]-1,oudeKop[1])
        
    if move == Move.DOWN: # and self.laatsteMove != Move.UP:
      if oudeKop[0] == self.frame.hoogte-1:
        if self.checkGrens:
          nieuweKop = oudeKop
        else:
          nieuweKop = (0,oudeKop[1])              
      else:
        nieuweKop = (oudeKop[0]+1,oudeKop[1])

    if move == Move.RIGHT: # and self.laatsteMove != Move.LEFT:
      if oudeKop[1] == self.frame.breedte-1:
        if self.checkGrens:
          nieuweKop = oudeKop
        else:
          nieuweKop = (oudeKop[0],0)
      else:
        nieuweKop = (oudeKop[0],oudeKop[1]+1)
    
    if move == Move.LEFT: # and self.laatsteMove != Move.RIGHT:
      if oudeKop[1] == 0:
        if self.checkGrens:
          nieuweKop = oudeKop
        else:
          nieuweKop = (oudeKop[0],self.frame.breedte -1)
      else:
        nieuweKop = (oudeKop[0],oudeKop[1]-1)
    #Checken of de nieuwe kop voedsel is
    if self.CheckVoedsel(nieuweKop):
    ###########################################
      self.voedsel = (random.randint(0,15),random.randint(0,15))
      #################################################
      print(self.voedsel)
    else:
      #Hier de nieuwe kop tonen
      self.pixelLijst.append(nieuweKop)
    #self.CheckMaxLengte()
    if self.groei == False:
      print("GRoei AF")
      del self.pixelLijst[0]
      print(self.pixelLijst)
    self.addToFrame(show)
    self.laatsteMove = move
  
  def addToFrame(self,show = True):
    self.frame.strip.clear_strip()
    #Toon de slang
    for x in range(len(self.pixelLijst)):          
      self.frame.zetKleur(self.pixelLijst[x][1],self.pixelLijst[x][0],self.kleur,100)
    #Toon het voedsel
    self.frame.zetKleur(self.voedsel[0],self.voedsel [1],self.voedselKleur,100)
    if show:
      self.frame.strip.show()

  def CheckVoedsel(self,kop):      
    if self.voedsel == kop:
      return True

  def CheckMaxLengte(self):
    if len(self.pixelLijst)<= self.maxLengte :
      self.groei = True
    else:
      self.groei = True
      