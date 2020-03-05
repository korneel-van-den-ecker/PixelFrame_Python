#!/usr/bin/env python3
import time
import math
import random
import pixelFrame
import sys
from enum import Enum

#print('Argument List:', str(sys.argv))


frame = pixelFrame.Frame(16, 16)
# frame.strip.global_brightness=1
kleur = 0x0000ff
kleur2 = 0xff0000
bright = 100
teller = 0
teller2 = 0
tellerBright = 1
kleuren = False
while 1:
    print('rééééééééééééévan Python')
    for line in sys.stdin:
        print(line)

    if teller < 255:
        teller += 1
    else:
        teller = 0
    if teller2 < 200:
        teller2 += 1
        kleuren = True
    else:
        teller2 = 0
        kleuren = False
    if kleuren:
        kleur = frame.strip.wheel(teller)
    else:
        kleur = 0x000000
    # if tellerBright <100:
        #tellerBright += 1
        #print (tellerBright)
    # else:
        #tellerBright = 0
    # frame.kleurRechthoek(kleur,0,0,15,15,1)
    # frame.kleurEffect(0xff0000,0x0000ff,0,0,15,15)
    # for x in range(50):

    xOffset = 0  # random.randint(0,15)
    yOffset = 0  # random.randint(0,15)
    x = teller % (16-xOffset) + xOffset
    y = teller % (16-yOffset) + yOffset
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)
    frame.zetKleur(random.randint(xOffset, x),
                   random.randint(yOffset, y), kleur, 1)

    frame.show()
    time.sleep(0.5)
    frame.strip.clear_strip()
    # time.sleep(0.05)
