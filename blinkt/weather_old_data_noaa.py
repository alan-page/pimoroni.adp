import json
import requests

from blinkt import set_pixel, set_brightness, show, clear
import time

# from datetime import datetime

import weather_constants

print weather_constants.NOAA_API_TOKEN
print weather_constants.NOAA_STATION_ID

response = {}
#response = requests.get("https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=5&stationid=weather_constants.NOAA_STATION_ID&startdate=2022-02-13&enddate=2022-02-14", headers={'token':weather_constants.NOAA_API_TOKEN})
response = requests.get("https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets", headers={'token':weather_constants.NOAA_API_TOKEN})
d = json.loads(response.text)

while False:
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

    print(starttime0 + " " + name0 + ": " + str(temp0) + " deg F")
    print("Forecast:  " + shortforecast0)
    print " "

    print(starttime1 + " " +name1 + ": " + str(temp1) + " deg F")
    print("Forecast:  " + shortforecast1)
    print " "

# Don't print third timeblock
#    print(starttime2 + " " + name2 + ": " + str(temp2) + " deg F")
#    print("Forecast:  " + shortforecast2)
#    print " "

    if  temp1 >= 50:
        print "It's going to be 50+ - Winter must be over!"

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
        set_pixel(1, 0, 5, 15)
        show()
        time.sleep(5)
        clear()

    if temp1 <= 10:
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

