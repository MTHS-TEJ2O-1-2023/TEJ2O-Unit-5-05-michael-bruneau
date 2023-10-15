"""
Created by: Michael Bruneau
Created on: Oct 2023
This module is a Micro:bit MicroPython program
neopixel_random.py
"""

from microbit import *
import neopixel
from random import randint

np = neopixel.NeoPixel(pin16, 5)

for pixel_id in range(0, len(np)):
    red = randint(0, 255)
    yellow = randint(0, 255)
    green = randint(0, 255)
    np[pixel_id] = (
        red,
        green,
        yellow,
    )

display.clear()
display.show(Image.HAPPY)
print(np[0])
np[0] = (0, 0, 0)
print(np[1])
np[1] = (0, 0, 0)
print(np[2])
np[2] = (0, 0, 0)
print(np[3])
np[3] = (0, 0, 0)
np.show()

while True:
    if button_a.is_pressed():
        display.clear()
        np[2] = (0, 255, 0)
        np.show()
        sleep(1000)
        np[2] = (0, 0, 0)
        np[1] = (255, 255, 0)
        np.show()
        sleep(1000)
        np[1] = (0, 0, 0)
        np[0] = (255, 0, 0)
        np.show()
        sleep(1000)
        np[0] = (0, 0, 0)
        np.show()
        display.show(Image.HAPPY)
