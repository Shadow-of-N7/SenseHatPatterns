#!/usr/bin/env python3

# Fills the matrix randomly and cleans up. All step by step.

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear()

c_pixels = []
for count in range(randint(0, 64)):
  x = randint(0,7)
  y = randint(0,7)
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  sense.set_pixel(x, y, r, g , b)
  if [x,y] not in c_pixels:
	  c_pixels.append([x,y])
  sleep(0.05)
sleep(0.3)

for pixel in c_pixels:
  sense.set_pixel(pixel[0],pixel[1],0,0,0)
  sleep(0.05)
sleep(0.3)