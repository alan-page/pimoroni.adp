#!/usr/bin/env python

import math
import time

import blinkt
import random

blinkt.set_clear_on_exit()


def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1
#   Print the pixel numbers; removed as it slowed the LED display
#    print "pixel " + str(v)
    blinkt.show()

#blinkt.set_brightness(1)
blinkt.set_brightness(0.033)
#blinkt.set_brightness(0.2)

try:
    while True: # Run constantly
#    for y in range(60): # Only run 60 iterations
        t = time.time()
#        print "time: ", t
        v = (math.sin(t) + 1) / 2  # Get a value between 0 and 1
              # Not just get a value between 0 and 1, get a sinewave of values "...sin(system time), 100 times per second"
              # Repeating this makes the bar go up and down, as the 0 to 1 values are fed into the above function and are spread 
              # across the eight LEDs...genius
        st = (math.sin(t))
#        print "math.sin(t): ", st

#        print "(math.sin(t) + 1 / 2: ", v
#        print round(v, 1)
        dots = v * 10
#        print '0 ' * int(dots) # Print an asterisk for each 0.1 rise in the sin(t) value
#        bluevalue = random.randint(0, 15)
#        redvalue = random.randint(0, 15)
        show_graph(v, 70, 0, 150)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
