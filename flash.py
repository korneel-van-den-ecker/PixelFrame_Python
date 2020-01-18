#!/usr/bin/env python3
from snake import Snake
from pixelFrame import Frame
#from xbox import*
import random
import time
import math
#import keyboard

frame = Frame(16,16)
rood = 0x00f0ff
hoogte = 16
breedte = 16
zoom = 1/2
factor = 2
speed = 100
aantalBeelden = math.ceil(speed/factor)
periode = math.pi *factor

while 1:
    #sinus
    for y in range(aantalBeelden):
        for x in range(breedte):
            #waarde van de hoek van 0 tem 360° 
            radiaalPositie = ((periode / breedte) * x) + (periode / aantalBeelden * y )
            #sinus waarde van -1.0 tem 1.0
            amplitude = math.sin(radiaalPositie)
            #herschalen naar aantal pixels in de hoogte
            frameAmplitude = math.ceil((hoogte/zoom) - amplitude*hoogte/zoom)
            if (frameAmplitude >= 16):
                frameAmplitude = 15
            frame.zetKleur(x,frameAmplitude,rood,1)
        frame.strip.show()
            #time.sleep(0.05)
        frame.strip.clear_strip()

    """ for x in range(breedte):
        #waarde van de hoek van 0 tem 360° 
        radiaalPositie = (math.pi * 2 / breedte) * x
        #sinus waarde van -1.0 tem 1.0
        amplitude = math.tan(radiaalPositie)
        #herschalen naar aantal pixels in de hoogte
        frameAmplitude = math.ceil((hoogte/zoom) - amplitude*hoogte/zoom)
        if (frameAmplitude == 16):
            frameAmplitude = 15
        frame.zetKleur(frameAmplitude,x,rood,1)
        frame.strip.show()
        time.sleep(0.05)
    frame.strip.clear_strip() """

