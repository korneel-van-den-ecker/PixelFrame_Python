#!/usr/bin/env python3
from snake import Snake
from snake import Move
from pixelFrame import Frame
import random
import time
#import keyboard

#keyboard.write('The quick brown fox jumps over the lazy dog.')

frame = Frame(16,16)
#frame.strip.max_speed_hz=1000000
frame.strip.global_brightness=100
snakes = [Snake(frame,4,2,0xff00ff),Snake(frame,4,2,0xffff00),Snake(frame,4,2,0x00ffff)]

while 1:
  frame.strip.clear_strip()
  for x in range(len(snakes)):    
    beweging = random.choice(list(Move))
    snakes[x].checkGrens = False
    snakes[x].move(beweging,False,False)
  frame.strip.show()  
  #time.sleep(float(random.randrange(1,10))/100)
  
frame.strip.clear_strip_show()
print(snakes)

