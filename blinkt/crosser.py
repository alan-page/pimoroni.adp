from blinkt import set_pixel, set_all, set_brightness, show, clear, NUM_PIXELS
import time

pixel_delay = 0.06
pause_delay = 0.1
pixel1_brightness = 0.033
pixel2_brightness = 0.07

#set_brightness(1)

while True:
	for i in range(8):
		clear()

# background color
#		set_all(10, 10, 10, pixel2_brightness)


# color 1/ color 2
		set_pixel(i, 255, 0, 200, pixel1_brightness)
		set_pixel(7 - i, 255, 25, 0, pixel2_brightness)

		show()
		time.sleep(pixel_delay)

#	clear()
#	show()
	time.sleep(pause_delay)

	for i in range(8):
		clear()

# background color
#		set_all(10, 10, 10, pixel2_brightness)

		set_pixel(i, 255, 25, 0, pixel2_brightness)
		set_pixel(7 - i, 255, 0, 200, pixel1_brightness)
		show()
		time.sleep(pixel_delay)

#	clear()
#	show()
	time.sleep(pause_delay)
