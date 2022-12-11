#!/usr/bin/env python3

from snake import Snake
from pixelFrame import Frame
#from xbox import*
import random
import time
#import keyboard

#keyboard.write('The quick brown fox jumps over the lazy dog.')

class FirePlace:
  def __init__(self):
    self.frame = Frame(16,16)
    #self.frame.strip.max_speed_hz=1500000
    self.frame.strip.global_brightness=1
    self.onderband = 2
    self.play = True
  def start(self):
    teller = 0
    bright = 100
    while self.play == True:
      self.frame.strip.clear_strip()
      for x in range(self.frame.breedte):
        for y in range(10):    
          if teller <86:  
            kleur = self.frame.strip.wheel(teller)
            teller += 1
          else:
            teller =66 
            print(kleur)
        self.frame.kleurRechthoek(kleur,x,int(random.randint(self.onderband,self.frame.hoogte-self.onderband)),x,self.frame.hoogte,bright) 
        print(bright)
      self.frame.strip.show()
      time.sleep(float(random.randrange(80,100))/1000)
  def stop(self):
    self.frame.release()
    self.play = False
    #self.frame.strip.clear_strip()
    #self.frame.strip.show()
fireplace = FirePlace()
fireplace.start()

