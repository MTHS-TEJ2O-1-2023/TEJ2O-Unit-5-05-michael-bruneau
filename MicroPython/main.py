"""
Created by: Michael Bruneau
Created on: Oct 2023
This module is a Micro:bit MicroPython program
neopixel_random.py
"""

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin16, 3)

for pixel_id in range(0, len(np)):
    red = range(0, 255)
    yellow = range(0, 255)
    Green = range(0, 255)
np[pixel_id] = (red, Green, yellow,)

display.clear()
display.show(Image.HAPPY)
print(np(0))
np[0] = (255, 0, 0)
print(np(1))
np[1] = (0, 0, 0)
print(np(2))
np[2] = (0, 0, 0)
print(np(3))
np[3] = (0, 0, 0)
np.show()
