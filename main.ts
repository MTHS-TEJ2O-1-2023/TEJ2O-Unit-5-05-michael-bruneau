/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Michael B
 * Created on: Oct 2023
 * This program diplays traffic lights on neopixels
*/

basic.clearScreen()
basic.showIcon(IconNames.Happy)

let neopixelStrip: neopixel.Strip = null

neopixelStrip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
