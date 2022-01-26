import json
import requests

from blinkt import set_pixel, set_brightness, show, clear
import time

while True:
    while True:
        try:
            print "Trying the weather API..."
            response = requests.get("http://api.weather.gov/gridpoints/OKX/51,69/forecast/")
            days = json.loads(response.text)
            name = days['properties']['periods'][1]['name']
            temp = days['properties']['periods'][1]['temperature']
            break
        except:
            print "Didn't get a response. Trying again."
            print " "

    print(name + ": " + str(temp))


    if 41 < temp < 50:
        print "It's going to be almost temperate. Probably sweater weather."
        set_pixel(4, 0, 20, 15)
        show()
        time.sleep(5)
        clear()

    if 31 < temp < 40:
        print "It's going to be cold. Better wear a coat."
        set_pixel(3, 0, 15, 15)
        show()
        time.sleep(5)
        clear() 

    if 21 < temp < 30:
        print "Better make it a warm coat."
        set_pixel(2, 0, 10, 15)
        show()
        time.sleep(5)
        clear()

    if 11 < temp < 20:
        print "Remember that really heavy parka..."
        set_pixel(1, 0, 5, 15)
        show()
        time.sleep(5)
        clear()

    if temp < 10:
        print "...And long underwear..."
        set_pixel(0, 0, 0, 15)
        show()
        time.sleep(5)
        clear()

    print " "
    print "Next update in 30 minutes"
    time.sleep(300)
    
    print "Next update in 25 minutes"
    time.sleep(300)

    print "Next update in 20 minutes"
    time.sleep(300)

    print "Next update in 15 minutes"
    time.sleep(300)

    print "Next update in 10 minutes"
    time.sleep(300)

    print "Next update in 05 minutes"
    time.sleep(300)
    print " "

