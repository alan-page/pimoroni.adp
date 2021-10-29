from blinkt import set_pixel, set_all, set_brightness, show, clear
import time
import random

set_brightness(0.2)
#set_brightness(1)

custom_brigthness = 1
sleep_time = 0.6

while True:
	pixel = random.randint(0, 7)
	pixel2  = random.randint(0, 7)
	pixel3  = random.randint(0, 7)
	color1 = random.randint(0, 15)
	color2 = random.randint(0, 15)
#	color3 = random.randint(0, 150)

# Set one of the colors to zero to produce less grey tones
	color3 = 0


	set_pixel(pixel, color1, color2, color3)
	set_pixel(pixel2, color2, color3, color1)
	set_pixel(pixel3, color3, color1, color2)
	show()
	time.sleep(sleep_time)

#	set_all(color1, color2, color3, custom_brigthness)
#       show()
#       time.sleep(sleep_time)


#	clear()
#	show()
#	time.sleep(0.05)
	
