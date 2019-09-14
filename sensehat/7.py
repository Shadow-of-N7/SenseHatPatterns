#!/usr/bin/env python3

# Creates a rainbow (sort of).

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear()

r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

r_reverse = False
b_reverse = False
g_reverse = False

for x in range(0, 8):
	for y in range(0, 8):
		sense.set_pixel(x, y, r, g, b)
		sense.set_pixel(y, x, r, g, b)
		
		if (r + 10) > 255:
			r_reverse = True
		if (g + 10) > 255:
			g_reverse = True
		if (b + 10) > 255:
			b_reverse = True
			
		if (r - 10) < 0:
			r_reverse = False
		if (g - 10) < 0:
			g_reverse = False
		if (b - 10) < 0:
			b_reverse = False
			
		if r_reverse is False:
			r += 10
		else:
			r -= 10
			
		if g_reverse is False:
			g += 10
		else:
			g -= 10	
			
		if b_reverse is False:
			b += 10
		else:
			b -= 10
			
		sleep(0.05)
		
sleep(1)

sense.clear()