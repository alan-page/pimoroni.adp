from blinkt import set_pixel, set_all, set_brightness, show, clear
import time


while True:
	set_all(255, 255, 255, 1)
	show()
	time.sleep(0.2)
        clear()
        show()
        time.sleep(0.2)
