from blinkt import set_pixel, set_brightness, show, clear
import time
import random

set_brightness(0.033)
#set_brightness(1)

while True:
	pixel = random.randint(0, 7)
#	set_pixel(pixel, 255, 255, 255)
	set_pixel(pixel, 255, 200, 155)
	show()
	time.sleep(0.1)
	clear()
	show()
	time.sleep(0.2)
	
