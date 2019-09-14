#!/usr/bin/env python3

# Creates funny inversed patterns.

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear()

r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

for iteration in range(0, 8):
	for x in range(0, 8):
		for y in range(0, 8):
			sense.set_pixel(x, y, r, g, b)
		sleep(0.05)
		
		for y in range(0, 8):
			sense.set_pixel(x, y, 0, 0, 0)
			
	for x in range(0, 8):
		for y in range(0, 8):
			sense.set_pixel(x, y, r, g, b)
		sleep(0.05)
		
		for y in range(0, 8):
			sense.set_pixel(y, x, 0, 0, 0)