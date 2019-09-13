#!/usr/bin/env python3

# Overwrites the matrix several times sequentially.

from sense_hat import SenseHat
from random import randint
from time import sleep
from sense_methods import sense_methods

sense = SenseHat()

sense.clear()

for iteration in range(0, 5):
	for pixel in range(0, 64):
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)
		sense_methods.set_pixel_in_array(pixel, r, g, b)
		sleep(0.05)