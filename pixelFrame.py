#!/usr/bin/env python3
from driver import apa102
import time
from enum import Enum

BREEDTE = 16
HOOGTE = 16
aantalLeds = 2

RED = 0xFF0000
GREEN = 0x00FF00
BLUE = 0x0000FF
class Frame:

  def __init__(self,breedte,hoogte):
    self.breedte = breedte
    self.hoogte = hoogte
    # Initialize the library and the strip
    self.strip = apa102.APA102(num_led=(breedte*hoogte), global_brightness=31, mosi = 10, sclk = 11,order='rgb')
  

  def show(self):
    self.strip.show()

  def zetKleur(self,x,y,kleur,brightness):
    #de x coordinaat omdraaien bij even rij
    if (y % 2) != 0 :
      x = self.breedte - 1 - x
    nummer = ((y*self.breedte)+x)
    #print(kleur)
    self.strip.set_pixel_rgb(nummer,kleur,brightness)  

  def kleurRechthoek(self,kleur,startX,startY,eindX,eindY,brightness):
    for x in range(startX,eindX+1):
      for y in range(startY,eindY+1):        
        self.zetKleur(x,y,kleur,brightness)

  def kleurEffect(self,kleur1,kleur2,startX,startY,eindX,eindY):
    print("#####################################################")
    print(format(kleur1,'02x'),format(kleur2,'02x'))    
    self.strip.clear_strip()
    channels1 = apa102.APA102.exctract_channels(kleur1)
    channels2 = apa102.APA102.exctract_channels(kleur2)
    while((channels1[0] != channels2[0]) or (channels1[1] != channels2[1]) or (channels1[2] != channels2[2])):
      for x in range(len(channels1)):
        print(format(channels1[x],'02x'))
      if channels1[0] < channels2[0]:
        channels1[0] += 1
      if channels1[0] > channels2[0]:
        channels1[0] -= 1
      if channels1[1] < channels2[1]:
        channels1[1] += 1
      if channels1[1] > channels2[1]:
        channels1[1] -= 1
      if channels1[2] < channels2[2]:
        channels1[2] += 1
      if channels1[2] > channels2[2]:
        channels1[2] -= 1
      self.kleurRechthoek(apa102.APA102.combine_color(channels1[0],channels1[1],channels1[2]),startX,startY,eindX,eindY,50)
      self.strip.show()
      #self.strip.clear_strip()
    print("EFFECT GEDAAN")
      #time.sleep(0.01)
  
    
  