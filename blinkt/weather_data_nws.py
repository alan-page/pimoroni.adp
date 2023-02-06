# Temp display on the Pimoroni Blinkt eight pixel RGB device

#print "import json"
import json

#print "import requests"
import requests

#print "import blinkt stuff"
from blinkt import set_pixel, set_brightness, show, clear

#print "import time" for the sleep() function
import time

#print "import datetime" for the datetime.now() function to display the date/time
import datetime

# LED rgb matrix with zero-based list corresponding to the temp bands
m = [
    [128,  32,  32],
    [  0,   0, 128],
    [  0,  64, 128],
    [  0, 128, 128],
    [  0, 128,   0],
    [128, 128,   0],
    [128,  64,   0],
    [128,   0,   0],
]
# print m

#Outer loop for displaying weather periodically
while True:
    #Inner loop for querying the weather API
    while True:
        try:
            print " "
            print " "
            print " "
            print "Querying the National Weather Service API..."

            # Had to add this initialization statement after putting the request in a try/catch.
            #
            # But it didn't seem to matter. It's as if the API is returning incorrect results,
            # but only 1 out of 10 requests...
            response = {}
            days = ''

            response = requests.get("http://api.weather.gov/gridpoints/OKX/51,69/forecast/")
            days = json.loads(response.text)
            name0 = days['properties']['periods'][0]['name']
            name1 = days['properties']['periods'][1]['name']

            temp0 = days['properties']['periods'][0]['temperature']
            temp1 = days['properties']['periods'][1]['temperature']

            shortforecast0 = days['properties']['periods'][0]['shortForecast']
            shortforecast1 = days['properties']['periods'][1]['shortForecast']

            starttime0 = days['properties']['periods'][0]['startTime']
            starttime1 = days['properties']['periods'][1]['startTime']
            break

        except:
            print " "
            print "No response. Trying again."
            print " "

# Print the next forecast block
    print(datetime.datetime.now())
    print " "
    print(starttime1 + " " +name1 + ": " + str(temp1) + " deg F (" + str(temp0) + " deg F during current period)")
    print("Next forecast:  " + shortforecast1)

# Clear the display

    clear()
    show()
# and wait
    time.sleep(1)

# Animation to show which temp we're displaying: upward sweep of the LEDs for the daily high?
# Downward sweep for now

    for y in range(7, -1, -1):
        set_pixel(y, m[y][0], m[y][1], m[y][2])
#        print y
        show()
# Print rgb values
#        print m[y]
        time.sleep(.03)
        clear()

    show()
    time.sleep(1)

    print " "
    if temp1 > 90:
        print "It's going to be over 90!"
        set_pixel(7, 255, 0, 0)
        show()

    if 80 <  temp1 <= 90:
        print "It's going to be over 80!"
        set_pixel(7, 225, 16, 16)
        show()

    if 70 < temp1 <= 80:
        print "It's going to be over 70!"
        set_pixel(7, 128, 0, 0)
        show()

    if 60 < temp1 <= 70:
        print "It's going to be over 60!"
        set_pixel(6, 128, 64, 0)
        show()

    if 50 < temp1 <= 60:
        print "It's going to be mild...winter must be over!"
        # One pixel higher at a lower intensity
        set_pixel(6, 32, 16, 0) 
        set_pixel(5, 128, 128, 0)
        # One pixel lower at a lower intensity
        set_pixel(4, 0, 32, 0)
        show()

    if 40 < temp1 <= 50:
        print "It's going to be almost temperate. Probably sweater weather."
        set_pixel(4, 0, 128, 0)
        show()

    if 30 < temp1 <= 40:
        print "It's going to be cold. Better wear a coat."
        set_pixel(3, 0, 128, 128)
        show()

    if 20 < temp1 <= 30:
        print "Wear the coat. Better make it a warm coat."
        set_pixel(2, 0, 64, 128)
        show()

    if 10 < temp1 <= 20:
        print "Remember that really heavy parka? Bring it."
        set_pixel(1, 0, 0, 128)
        show()

    if 0 < temp1 <= 10:
        print "Brr! Bring the parka and wear long underwear..."
        set_pixel(0, 128, 64, 64)
        show()

    if temp1 <= 0:
        print "Oh boy! Below zero--add the balaclava."
        for x  in range(5):
            set_pixel(0, 128, 128, 128)
            show()

    print " "
    print "Next update in 10 minutes"
    time.sleep(600)


