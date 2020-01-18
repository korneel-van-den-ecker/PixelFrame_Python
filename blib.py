#!/usr/bin/env python3
import time
import math
import random
import pixelFrame
from enum import Enum

frame = pixelFrame.Frame(16,16)
frame.strip.global_brightness=1
kleur = 0x0000ff
kleur2 = 0xff0000
bright = 100
teller = 0
teller2 = 0
tellerBright = 1
kleuren = True
while 1: 
  if teller <255:    
    teller += 1
  else:
    teller = 0
  if teller2 <200:
    teller2+= 1
    kleuren = True
  else:
    teller2 = 0  
    kleuren = False
  if kleuren:
    kleur = frame.strip.wheel(teller)
  else:
    kleur = 0x000000
  if tellerBright <100:
    tellerBright += 1
    print (tellerBright)
  else: 
    tellerBright = 0
  frame.zetKleur(random.randint(0,frame.breedte),random.randint(0,frame.hoogte),kleur,tellerBright)
  frame.strip.show()
  time.sleep(0.03)
  #frame.strip.clear_strip()
  #time.sleep(0.05)