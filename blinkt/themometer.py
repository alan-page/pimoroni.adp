from blinkt import set_pixel, set_brightness, show, clear
import time
import random

set_brightness(0.033)
#set_brightness(1)

t = 25

while True:

	if t < 30:
		set_pixel(7, 0, 255, 255)

	elif t < 40:
		set_pixel(6, 0, 127, 255)

	elif t < 50:
		set_pixel(5, 127, 127, 0)

	elif t < 60:
		set_pixel(4, 127, 255, 0)

	elif t < 70:
		set_pixel(3, 255, 255, 0)

	elif t < 80:
		set_pixel(2, 255, 99, 0)

	elif t < 90:
		set_pixel(1, 255, 66, 0)

	elif t > 99:
		set_pixel(0, 255, 0, 0)

#	set_pixel(pixel, 255, 255, 255)
#	set_pixel(pixel, 255, 200, 155)
	show()
	time.sleep(0.1)
#	clear()
#	show()
#	time.sleep(0.2)
	
