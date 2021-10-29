from blinkt import set_pixel, set_brightness, show, clear
import time

time_delay = 0.1

#set_brightness(1)

while True:
	for i in range(1, 8, 1):
		clear()
# Tungsten
#		set_pixel(i, 255, 214, 170)

# Red
		set_pixel(i, 255, 0, 0)

# White
#		set_pixel(i, 255, 255, 255)
		set_brightness(0.19)

		show()
		time.sleep(time_delay)
		clear()


	for i in range(6, -1, -1):
		clear()
# Green
		set_pixel(i, 0, 255, 0)
# Less brightness because green is so much brighter 
		set_brightness(0.033)
		show()
		time.sleep(time_delay)
		clear()
