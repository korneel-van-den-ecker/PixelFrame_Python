import pixelFrame
import time
import math
import random

frame = pixelFrame.Frame(16,16)
frame.strip.global_brightness=31
#for x in range(100):
#  frame.kleurRechthoek(2,2,13,13,0x0000ff)
#  frame.strip.show()
#  time.sleep(1)
teller =0
while 1:
  #kleur = 0xffffff #(0xff | (random.randint(0,255)<<8)|(random.randint(0,255)))
  for x in range(16):    
    if teller <255:  
      kleur = frame.strip.wheel(teller)
      teller += 1
    else:
      teller =0
    print(kleur)
    frame.kleurRechthoek(kleur,random.randint(0,15),random.randint(0,15),random.randint(0,15),random.randint(0,15),100)
    frame.strip.show()  
    print("1111STE")       
    time.sleep(0.05)
    #frame.strip.clear_strip()
    #time.sleep(0.01)
while 1:    
  for x in range(8):    
    if teller <255:  
      kleur = frame.strip.wheel(teller)
      teller += 1
    else:
      teller =0
    print(kleur)
    frame.kleurRechthoek(kleur,x,x,15-x,15-x)
    frame.strip.show()  
    print("1111STE")       
    time.sleep(0.1)
    #frame.strip.clear_strip()
    time.sleep(0.01)
    #frame.kleurEffect(0xff0000,0x00ff00,x,0,15,15)
    #frame.kleurEffect(0x00ff00,0x0000ff,x,0,15,15)
    #frame.kleurEffect(0x0000ff,0xff0000,x,0,15,15)
   
  for x in range(8,0,-1):    
    if teller <255:  
      kleur = frame.strip.wheel(teller)
      teller += 1
    else:
      teller =0
    print(kleur)
    frame.kleurRechthoek(kleur,x,x,16-x,16-x)
    frame.strip.show()        
    print("nuuuu") 
    time.sleep(0.1)
    #frame.strip.clear_strip()
    time.sleep(0.01)
    #frame.kleurEffect(0xff0000,0x00ff00,x,0,15,15)
    #frame.kleurEffect(0x00ff00,0x0000ff,x,0,15,15)
    #frame.kleurEffect(0x0000ff,0xff0000,x,0,15,15) 
    
#frame.strip.clear_strip_show()  