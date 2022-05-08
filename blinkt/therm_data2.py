import json
import requests

from blinkt import set_pixel, set_brightness, show, clear
import time

response = requests.get("http://api.weather.gov/gridpoints/OKX/51,69/forecast/")
days = json.loads(response.text)

print ''
print ''

for forecastNum in range(4):
# Print whole forecoasts
#    print (days['properties']['periods'][forecastNum]

# Print beginnin and end of forecasts
    print ('Start: ' + days['properties']['periods'][forecastNum]['startTime']
        + '     End: ' + days['properties']['periods'][forecastNum]['endTime']
        + '     ' + days['properties']['periods'][forecastNum]['name'])
    print ''

print ''

#ugly docstring multi-line comment
#
#
"""
forecast0 = days['properties']['periods'][0]
forecast1 = days['properties']['periods'][1]
forecast2 = days['properties']['periods'][2]


#name = days['properties']['periods'][0]['name']
#temp = days['properties']['periods'][0]['temperature']
#print(name + ": " + str(temp)) 

print(forecast0)
print ' ' 
print(forecast1)
print ' '
print(forecast2)
print ' ' 
"""
#end docstring


temp = 35

if temp < 40:
    print "It's going to be cold tomorrow. Better wear a coat."
    set_pixel(3, 0, 15, 15)
    show()
    time.sleep(5)
    clear()

if temp < 30:
    print "Better make it a warm coat."
    set_pixel(2, 0, 5, 15)
    show()
    time.sleep(5)
    clear()

if temp < 20:
    print "Remember that really heavy parka..."
    set_pixel(1, 0, 10, 15)
    show()
    time.sleep(5)
    clear()

if temp < 10:
    print "...And long underwear..."
    set_pixel(0, 0, 0, 15)
    show()
    time.sleep(5)
    clear()

