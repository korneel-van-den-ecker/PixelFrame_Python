#!/usr/bin/env python3
from snake import*
from pixelFrame import*
from xbox import*
import random
import time
import keyboard

frame = pixelFrame.Frame(16,16)
frame.strip.global_brightness=31
#for x in range(100):
#  frame.kleurRechthoek(2,2,13,13,0x0000ff)
#  frame.strip.show()
#  time.sleep(1)
teller =0
while 1:
  kleur = 0xff0000 #(0xff | (random.randint(0,255)<<8)|(random.randint(0,255)))
  for y in range(16):    
    for x in range(16):      
      for z in range(100,0,-25):
        if x%2==0:
          k=x
          x=y
          y=k
        frame.kleurRechthoek(kleur,x,x,y,y,z)
        #frame.kleurRechthoek(kleur,x,y+1,x,y+1,z)
        #frame.kleurRechthoek(kleur,x,y+2,x,y+2,z)      
        frame.strip.show()
        #time.sleep(0.05)
        frame.strip.clear_strip()
  