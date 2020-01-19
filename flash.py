#!/usr/bin/env python3
from pixelFrame import Frame
from sinus import Sinus
import random
import time
import math

frame = Frame(16,16)

rood = 0xff0000
blauw = 0x0000ff
#hoogte = frame.hoogte
breedte = frame.breedte

AANTALFRAME = 50000

sinussen = [Sinus(1,2,frame)]        

while 1:

    #sinus
    # Hier moet je het aantalbeelden geven van de sinus met de minste periode

    for y in range(sinussen[0].aantalBeelden):
        sinussen[0].VoegSinusToe(rood,y)
        #sinussen[1].VoegSinusToe(blauw,y)
        #sinussen[2].VoegSinusToe(0x00ff00,y)
        frame.strip.show()
            #time.sleep(0.05)
        frame.strip.clear_strip()