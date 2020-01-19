#!/usr/bin/env python3
from pixelFrame import Frame
#from xbox import*
import random
import time
import math

frame = Frame(16,16)

rood = 0xff0000
blauw = 0x0000ff
AANTALFRAME = 500

class Sinus:
    def __init__(self,periode,zoom,frame):
        self.factorPeriode = periode * 2 
        self.speed = AANTALFRAME/periode
        self.aantalBeelden = math.ceil(self.speed/self.factorPeriode)
        self.periode = math.pi *self.factorPeriode
        self.frame = frame
        self.zoom = zoom
 
    def VoegSinusToe(self,kleur,huidigBeeld):
        for x in range(self.frame.breedte):
            #waarde van de hoek van 0 tem 360° 
            radiaalPositie = ((self.periode / self.frame.breedte) * x) + (self.periode / self.aantalBeelden * huidigBeeld )
            #sinus waarde van -1.0 tem 1.0
            # DE BEWERKING altijd herschalen van -1 tot 1
            # sin
            #amplitude = math.sin(radiaalPositie)
            # cin
            #amplitude = math.sin(radiaalPositie)
            # exp
            #amplitude = math.pow(radiaalPositie/10,4)
            # linair
            #amplitude = radiaalPositie/5 /2
            #herschalen naar aantal pixels in de hoogte
            frameAmplitude = math.ceil((self.frame.hoogte/self.zoom) - amplitude*self.frame.hoogte/self.zoom)
            if (frameAmplitude >= 15):
                frameAmplitude = 15
            self.frame.zetKleur(x,frameAmplitude,kleur,1)