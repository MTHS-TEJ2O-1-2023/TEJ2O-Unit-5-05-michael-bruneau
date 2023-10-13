"""
Created by: Michael Bruneau
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *

neopixel_strip = neopixel.NeoPixel(pin16, bpp=3)
neopixel_strip[0] = (0, 0, 0)
neopixel_strip.show()
display.clear()
display.show(Image.HAPPY)
