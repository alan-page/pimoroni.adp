#!/usr/bin/python
from blinkt import set_pixel, set_brightness, show, clear
import time

# RPi.GPIO library
import RPi.GPIO as GPIO

time_delay = 0.1

#set_brightness(1)

lead_brightness = 0.2
tail_brightness = 0.033


while True:
	for i in range(1, 8, 1):
		clear()
# Tungsten
#		set_pixel(i, 255, 214, 170)

# Red
		set_pixel(i, 255, 0, 0, lead_brightness)
		set_pixel(i-1, 255, 0, 0, tail_brightness)
# White
#		set_pixel(i, 255, 255, 255)
#		set_brightness(0.033)

		show()
		time.sleep(time_delay)
		clear()


	for i in range(6, -1, -1):
		clear()
		set_pixel(i, 255, 0, 0, lead_brightness)
		set_pixel(i+1, 255, 0, 0, tail_brightness)
		show()
		time.sleep(time_delay)
		clear()
