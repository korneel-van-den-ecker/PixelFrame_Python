#!/usr/bin/env python3
"""Ultra simple sample on how to use the library"""
from driver import apa102
import time

color = 0xFF0000
# Initialize the library and the strip
strip = apa102.APA102(num_led=256, global_brightness=10, mosi = 10, sclk = 11,
                                  order='rbg',max_speed_hz=900000)

# Turn off all pixels (sometimes a few light up when the strip gets power)
strip.clear_strip()

# Prepare a few individual pixels
for pix in range(256):
	for aantal in range(pix,pix+3):
		strip.set_pixel_rgb(aantal,color)
	strip.show()
	time.sleep(0.05)
	strip.set_pixel_rgb(aantal,0x000000)
#strip.set_pixel_rgb(12, 0xFF0000) # Red
#strip.set_pixel_rgb(24, 0xFFFFFF) # White
#strip.set_pixel_rgb(40, 0x00FF00) # Green
#print(strip)
# Copy the buffer to the Strip (i.e. show the prepared pixels)
#strip.show()

# Wait a few Seconds, to check the result
time.sleep(2)

# Clear the strip and shut down
strip.clear_strip()
strip.show()
strip.cleanup()

