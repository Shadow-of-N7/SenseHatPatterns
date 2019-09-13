#!/usr/bin/env python3

# Randomly lights up pixels.

import random
from sense_hat import SenseHat
from random import randint
from time import sleep
from sense_methods import sense_methods

sense = SenseHat()

sense.clear()

for i in range (0, randint(0, 256)):
	x = randint(0, 7)
	y = randint(0, 7)
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	sense.set_pixel(x, y, r, g, b)
	sleep(random.uniform(0.01, 0.2))
	sense.set_pixel(x, y, 0, 0, 0);