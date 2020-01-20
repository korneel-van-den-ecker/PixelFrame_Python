#!/usr/bin/env python3
from pixelFrame import Frame
#from xbox import*
import random
import time
import math

frame = Frame(16,16)

rood = 0xff0000
blauw = 0x0000ff
bovenGrafiek = 0xff0000
onderGrafiek = 0x00ff00
AANTALFRAME = 200

class Sinus:
    def __init__(self,periode,zoom,frame):
        self.factorPeriode = periode * 2 
        self.speed = AANTALFRAME/periode
        self.aantalBeelden = math.ceil(self.speed/self.factorPeriode)
        self.periode = math.pi * self.factorPeriode
        self.frame = frame
        self.zoom = zoom
        self.brightTeller = 0.0
        self.brightRichting = True
        self.aantalFrame = 0
        self.kleurBovenGrafiek = 0xff0000
        self.kleurOnderGrafiek = 0x0000ff
        self.kleurLijn = 0x000000
        self.start = True
        self.teller = 0

    def VoegSinusToe(self,huidigBeeld,bewerking):
        self.aantalFrame = self.aantalFrame + 1

        # Achtergrond ondergraffiek
        self.frame.kleurRechthoek(self.kleurOnderGrafiek,0,0,15,15,1)

        for x in range(self.frame.breedte):
            #waarde van de hoek van 0 tem 360° 
            radiaalPositie = ((self.periode / self.frame.breedte) * x) + (self.periode / self.aantalBeelden * huidigBeeld )
            #sinus waarde van -1.0 tem 1.0
            # DE BEWERKING altijd herschalen van -1 tot 1
            if(bewerking == "cos"):
                amplitude = math.cos(radiaalPositie)
            if(bewerking == "sin"):
                amplitude = math.sin(radiaalPositie)

            #pulse met de sync f functie https://nl.wikipedia.org/wiki/Sinc-functie
            if(bewerking == "pulse"):
                radiaalPositie = radiaalPositie - 2* math.pi
                if( radiaalPositie == 0):
                    amplitude = 1
                else:
                    amplitude = math.sin(math.pi * radiaalPositie)/(math.pi*radiaalPositie)
            if(bewerking == "tan"):
                amplitude = math.tan(radiaalPositie) 
            if(bewerking == "pow"):
                amplitude = math.pow(radiaalPositie/5,2)  
            if(bewerking == "lin"):
                amplitude = radiaalPositie/5 /2
            if(bewerking == "sqrt"):
                amplitude = math.sqrt(radiaalPositie/2) - 1
            #herschalen naar aantal pixels in de hoogte
            if(bewerking == "cos" or bewerking == "sin" or bewerking == "tan" or bewerking == "pulse"):
                frameAmplitude = math.ceil((self.frame.hoogte/self.zoom) - amplitude*self.frame.hoogte/self.zoom)
            if(bewerking == "pow" or bewerking == "lin" or bewerking == "sqrt" ):
                frameAmplitude = math.ceil(self.frame.hoogte - amplitude*self.frame.hoogte)                
            if (frameAmplitude >= 15):
                frameAmplitude = 15



            """ if(self.brightRichting == True):
                self.brightTeller = self.brightTeller + 0.15
            else:
                self.brightTeller = self.brightTeller - 0.95
            bright = math.ceil(self.brightTeller)
            if(bright == 100):
                self.brightRichting = False
            if(bright == 1):
                self.brightRichting = True
            self.frame.zetKleur(x,frameAmplitude,kleur,bright)  """   

            # pulse op de grafiek
            if(x == self.aantalFrame%AANTALFRAME):
                self.frame.zetKleur(x,frameAmplitude,0xffffff,100)            
            else:
                self.frame.zetKleur(x,frameAmplitude,self.kleurLijn,1)

            #normaal
            #self.frame.zetKleur(x,frameAmplitude,kleur,1)         
            
            #onder (gekleurd boven grote if) en bovenGrafiek Kleurn
            for y in range(0,frameAmplitude):
                self.frame.zetKleur(x,y,bovenGrafiek,1)        

    def showFrame(self):
        self.frame.strip.show()
        #time.sleep(0.05)
        self.frame.strip.clear_strip()
    
    def startAnimatie(self,bewerking):

        while self.start:
            for y in range(self.aantalBeelden):
                self.teller = math.ceil( self.teller + 1 )                
                print(self.teller)
                #frame.strip.wheel((teller%100)+40)
                #frame.strip.wheel((teller%100)+75)
                0x000000 
                self.VoegSinusToe(y,bewerking)
                self.showFrame()