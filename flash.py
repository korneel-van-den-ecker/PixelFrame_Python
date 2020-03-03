#!/usr/bin/env python3
from pixelFrame import Frame
from functieGenerator import FunctieGenerator, Functie
import random
import time
import math

frame = Frame(16,16)

rood = 0x000000
blauw = 0x0000ff
hoogte = frame.hoogte
breedte = frame.breedte
teller = 0
teller1 = 0
#sinussen = [Sinus(1,2.5,frame)]#,Sinus(2,1/22,frame)]#,Sinus(1,1,frame)]        
 
""" sinus = Sinus(1,2,frame)
sinus.brightnessEffect = False
sinus.flikkeringEffect = False
sinus.startAnimatie("sin",1.0,0.0) """


fg = FunctieGenerator(1,2,frame)
fg.flikkeringEffect = True
fg.VoegFunctieToe(Functie("sin",1/2,1))
#fg.VoegFunctieToe(Functie("sin",1,0))
fg.startAnimatie()