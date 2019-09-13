#!/usr/bin/env python3

# Send a pixel along the lines.

from sense_methods import sense_methods
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
for position in range(0, 64):
  sense.clear()
  sense_methods.set_pixel_in_array(position, r, g, b)
  sleep(0.05)
sense.clear()
