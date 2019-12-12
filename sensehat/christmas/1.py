#!/usr/bin/env python3

# Falling snowflakes

import random
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear()

class Flake:
    x_pos = randint(0, 7)
    y_pos = -1
    r = 150
    g = 150
    b = 150

    def __init__(self):
        self.x_pos = randint(0, 7)
        self.y_pos = randint(0, 7)
        pass

    def fall(self):
        sense.set_pixel(self.x_pos, self.y_pos, 0, 0 , 0)
        if self.y_pos == 7:
            self.y_pos = -1
            self.x_pos = randint(0, 7)
        self.y_pos += 1
        sense.set_pixel(self.x_pos, self.y_pos, self.r, self.g , self.b)


flakes = []
for x in range(0, 14):
    flakes.append(Flake())

iterations = 0

while iterations < 32:
    iterations += 1
    for flake in range(0, len(flakes)):
        flakes[flake].fall()
        sleep(random.random())
        #sleep(random.random(0.1, 0.18))


