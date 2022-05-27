#!/usr/bin/env python3
from snake import Snake
from pixelFrame import Frame
from snake import Move
# from xbox import Xbox
import random
import time
import keyboard

#keyboard.write('The quick brown fox jumps over the lazy dog.')

class SnakeGame:
  def __init__(self,aantalSnakes,frame):
    self.frame = frame
    self.tellers = [] 
    self.snakes = [] 
    self.maakSnakes(aantalSnakes)
    
        
  def maakSnakes(self,aantalSnakes):
    #snakes aanmaken
    for x in range(aantalSnakes):
      snake = Snake(frame,2,2,0xff0000)
      self.snakes.append(snake)
    
    #tellers instellen
    for x in range(aantalSnakes):
      self.tellers.append(int(255/aantalSnakes*x))
      
  def startAnimatie(self):    
    teller = 0
    while 1:
      self.frame.strip.clear_strip()
        
      #bepalen van kleur        
      self.kleurVerloop()
        
      #bepalen van lengte en positie
      for x in range(len(self.snakes)):
        if teller == 0:
          beweging = random.choice(list(Move))        
        self.snakes[x].checkGrens = True
        self.snakes[x].maxLenght = 20          
        self.snakes[x].move(beweging,True,False)
      self.frame.strip.show()  
      #time.sleep(float(random.randrange(50,55))/1000)
      if teller == 5:
        teller = 0
      else:
        teller = teller + 1    

  def kleurVerloop(self):
    for x in range(len(self.snakes)):
      if self.tellers[x] <255:  
        kleur = self.frame.strip.wheel(self.tellers[x])
        self.tellers[x] += 1
        self.snakes[x].kleur = kleur
        self.snakes[x].voedselKleur = kleur
      else:
        self.tellers[x] =0
      
              
  def close_clean(self):
    print('Interrupted...')
    """Cleanup method."""
    self.frame.strip.clear_strip()
    self.frame.strip.cleanup()   
    
                  
frame = Frame(16,16)
#frame.strip.max_speed_hz=150000
frame.strip.global_brightness=1
game = SnakeGame(1,frame)

game.startAnimatie()
  
#snake.frame.strip.clear_strip_show()
#print(snake)

