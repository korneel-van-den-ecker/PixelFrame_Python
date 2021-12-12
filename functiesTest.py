#!/usr/bin/env python3
from pixelFrame import Frame
from functieGenerator import FunctieGenerator, Functie
import random
import time
import math

frame = Frame(16, 16)


""" sinus = Sinus(1,2,frame)
sinus.brightnessEffect = False
sinus.flikkeringEffect = False
sinus.startAnimatie("sin",1.0,0.0) """


# periode,zoom
fg = FunctieGenerator(1, 1, frame)
#fg.flikkeringEffect = True
fg.brightnessEffect = True

# amplitude fasedaraai
#fg.VoegFunctieToe(Functie("sin", 2, 1))
fg.VoegFunctieToe(Functie("sin", 4, 1))
fg.VoegFunctieToe(Functie("sin", 4, 2))
#fg.VoegFunctieToe(Functie("cos", 1, 1))
fg.startAnimatie()
