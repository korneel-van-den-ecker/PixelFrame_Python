#!/usr/bin/env python3
from snake import*
from pixelFrame import*
from xbox import*
import random
import time
import keyboard

#keyboard.write('The quick brown fox jumps over the lazy dog.')

class FirePlace:
  def __init__(self):
    self.frame = pixelFrame.Frame(16,16)
    self.frame.strip.max_speed_hz=80000
    self.frame.strip.global_brightness=31
    self.onderband = 4
 
         
  def start(self):
    teller = 0
    bright = 100
    while 1:
      self.frame.strip.clear_strip()
      for x in range(self.frame.breedte):
        for y in range(10):    
          if teller <85:  
            kleur = self.frame.strip.wheel(teller)
            teller += 1
          else:
            teller =60  
            print(kleur)
        self.frame.kleurRechthoek(kleur,int(random.randint(self.onderband,self.frame.hoogte-self.onderband)),x,self.frame.hoogte,x,bright) 
        print(bright)
      self.frame.strip.show()
      time.sleep(float(random.randrange(20,50))/1000)
      
    
fireplace = FirePlace()
fireplace.start()

