from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Simply canges the screen color over time. Lights up until white, then goes dark again.
r = 0
g = 0
b = 0
full = False

while not (full is True and r == 0 and g == 0 and b == 0):
	if full is False:
		if r < 255:
			r += 1
		if r == 255 and g < 255:
			g += 1
		if r == 255 and g == 255 and b < 255:
			b += 1
		if r == 255 and g == 255 and b == 255:
			full = True
	if full is True:
		if r > 0 and g == 255 and b == 255:
			r -= 1
		if r == 0 and g > 0 and b == 255:
			g -= 1
		if r == 0 and g == 0 and b > 0:
			b -= 1
	sense.clear(r, g, b)
	
sense.clear()
