"""
Created by: Michael Bruneau
Created on: Oct 2023
This module is a Micro:bit MicroPython program
neopixel_random.py
"""

from microbit import *
import neopixel

# setup
np = neopixel.NeoPixel(pin16, 5)

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

# loop
while True:
    # Button A Pressed
    if button_a.is_pressed():
        display.clear()

        # neopixel 2 turn green
        np[2] = (0, 255, 0)
        np.show()
        sleep(1000)

        # turn off neopixel 2 and turn on neopixel 1 to yellow
        np[2] = (0, 0, 0)
        np[1] = (255, 255, 0)
        np.show()
        sleep(1000)

        # Turn off neopixel 1 and turn on neopixel 0 to red
        np[1] = (0, 0, 0)
        np[0] = (255, 0, 0)
        np.show()
        sleep(1000)

        # turn off neopixel 0
        np[0] = (0, 0, 0)
        np.show()
        display.show(Image.HAPPY)
