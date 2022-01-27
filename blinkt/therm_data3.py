import json
import requests

from blinkt import set_pixel, set_brightness, show, clear
import time

while True:
    while True:
        try:
            print "Trying the weather API..."
            
            # Had to add this initialization statement after putting the request in a try/catch, because
            # it seemed to have been adding each request results to the beginning of the dict item
            #
            # But it didn't seem to matter. It's as if the API is returning incorrect results,
            # but only 1 out of 10 requests...
            response = {}
            #
            response = requests.get("http://api.weather.gov/gridpoints/OKX/51,69/forecast/")
            days = json.loads(response.text)
            name = days['properties']['periods'][1]['name']
            temp = days['properties']['periods'][1]['temperature']
            shortforecast = days['properties']['periods'][1]['shortForecast']
            break
        except:
            print "Didn't get a response. Trying again."
            print " "

    print(name + ": " + str(temp) + " deg F")
    print("Forecast:  " + shortforecast)


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
        print "Wear the coat. Better make it a warm coat."
        set_pixel(2, 0, 10, 15)
        show()
        time.sleep(5)
        clear()

    if 11 < temp < 20:
        print "Remember that really heavy parka? Bring it."
        set_pixel(1, 0, 5, 15)
        show()
        time.sleep(5)
        clear()

    if temp < 10:
        print "Brr! Bring the parka and wear long underwear..."
        set_pixel(0, 0, 0, 15)
        show()
        time.sleep(5)
        clear()

    print " "
    print "Next update in 6 minutes"
    time.sleep(60)
    
    print "Next update in 5 minutes"
    time.sleep(60)

    print "Next update in 4 minutes"
    time.sleep(60)

    print "Next update in 3 minutes"
    time.sleep(60)

    print "Next update in 2 minutes"
    time.sleep(60)

    print "Next update in 1 minute"
    time.sleep(60)
    print " "

