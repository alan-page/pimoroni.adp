print "import json"
import json

print "import requests"
import requests

print "import blinkt stuff"
from blinkt import set_pixel, set_brightness, show, clear

print "import time"
import time

# LED rgb matrix with zero-based list corresponding to the temp bands
m = [
    [ 0 , 0, 15],
    [ 0,  5, 15],
    [ 0, 10, 15],
    [ 0, 15, 15],
    [ 0, 20, 15],
    [10, 20, 15],
    [20, 20, 10],
    [25, 20, 10],
]
print m

while True:
    while True:
        try:
            print "Trying the weather API..."
            print " "

            # Had to add this initialization statement after putting the request in a try/catch, because
            # it seemed to have been adding each request results to the beginning of the dict item
            #
            # But it didn't seem to matter. It's as if the API is returning incorrect results,
            # but only 1 out of 10 requests...
            response = {}
            #
            response = requests.get("http://api.weather.gov/gridpoints/OKX/51,69/forecast/")
            days = json.loads(response.text)
            name0 = days['properties']['periods'][0]['name']
            name1 = days['properties']['periods'][1]['name']
            name2 = days['properties']['periods'][2]['name']
            temp0 = days['properties']['periods'][0]['temperature']
            temp1 = days['properties']['periods'][1]['temperature']
            temp2 = days['properties']['periods'][2]['temperature']
            shortforecast0 = days['properties']['periods'][0]['shortForecast']
            shortforecast1 = days['properties']['periods'][1]['shortForecast']
            shortforecast2 = days['properties']['periods'][2]['shortForecast']
            starttime0 = days['properties']['periods'][0]['startTime']
            starttime1 = days['properties']['periods'][1]['startTime']
            starttime2 = days['properties']['periods'][2]['startTime']
            break
        except:
            print " "
            print "Didn't get a response. Trying again."
            print " "

#Don't print the first timeblock
#    print(starttime0 + " " + name0 + ": " + str(temp0) + " deg F")
#    print("Now forecast:  " + shortforecast0)
#    print " "

    print(starttime1 + " " +name1 + ": " + str(temp1) + " deg F")
    print("Next forecast:  " + shortforecast1)
    print " "

# Don't print third timeblock
#    print(starttime2 + " " + name2 + ": " + str(temp2) + " deg F")
#    print("Forecast:  " + shortforecast2)
#    print " "

# Animation to show which temp we're displaying: upward sweep of the LEDs for the daily high?
# This should really be in a loop...

    for y in range(7, -1, -1):
        set_pixel(y, m[y][0], m[y][1], m[y][2])
        show()
# Print rgb values
        print m[y]
        time.sleep(.5)
        clear()

    if temp1 > 80:
        print "It's going to be over 80!"
        set_pixel(7, 30, 10, 10)
        show()
        time.sleep(.5)
        clear()
        show()
        time.sleep(.5)
        set_pixel(7, 30, 10, 10)
        show()

    if 70 < temp1 <= 80:
        print "It's going to be over 70!"
        set_pixel(7, 25, 20, 10)
        show()
        
    if 60 < temp1 <= 70:
        print "It's going to be over 60!"
        set_pixel(6, 20, 20, 10)
        show()
        time.sleep(5)
        clear()

    if 50 < temp1 <= 60:
        print "It's going to be mild...winter must be over!"
        set_pixel(5, 10, 20, 15)
        show()
        time.sleep(5)
        clear()

    if 40 < temp1 <= 50:
        print "It's going to be almost temperate. Probably sweater weather."
        set_pixel(4, 0, 20, 15)
        show()
        time.sleep(5)
        clear()

    if 30 < temp1 <= 40:
        print "It's going to be cold. Better wear a coat."
        set_pixel(3, 0, 15, 15)
        show()
        time.sleep(5)
        clear() 

    if 20 < temp1 <= 30:
        print "Wear the coat. Better make it a warm coat."
        set_pixel(2, 0, 10, 15)
        show()
        time.sleep(5)
        clear()

    if 10 < temp1 <= 20:
        print "Remember that really heavy parka? Bring it."
        for x in range(5):
            set_pixel(1, 0, 5, 15)
            show()
            time.sleep(.5)
            clear()
            # For some reason clear() doesn't blank the display here
            set_pixel(1, 0, 0, 0)
            show()
            time.sleep(.5)
        set_pixel(1, 0, 5, 15)
        show()

    if 0 < temp1 <= 10:
        print "Brr! Bring the parka and wear long underwear..."
        set_pixel(0, 0, 0, 15)
        show()
        time.sleep(5)
        clear()

    if temp1 <= 0:
        print "Oh boy! Below zero--add the balaclava."
        for x  in range(5):
            set_pixel(0, 0, 0, 15)
            show()
            time.sleep(0.5)
            # Might need a show() blank pixel here; see < 20 above
            clear()
            time.sleep(0.5)

    print " "
    print "Next update in 1 minute"
    time.sleep(60)
    print " "


