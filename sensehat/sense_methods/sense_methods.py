from sense_hat import SenseHat

sense = SenseHat()

def set_pixel_in_array(position, r, g, b):
  x_pos = (position % 8) 
  y_pos = int(position // 8)
  if position  == 0:
    x_pos = 0
    y_pos = 0
  sense.set_pixel(x_pos, y_pos, r, g, b)
