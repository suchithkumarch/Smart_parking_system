import urllib.request
import requests
import threading
import json
import random
import time
import board
import adafruit_hcsr04
sonar1 = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
sonar2 = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D27)
# Define a function to get status of parking lots from the distance 
def get_status(distance):
    if(distance<10):
        return 2
    elif(distance<50):
        return 1
    else:
        return 0
# Define a function that will post on server every 15 Seconds
def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    dist1=sonar1.distance
    dist2=sonar2.distance
    URl='https://api.thingspeak.com/update?api_key='
    KEY='BLDX37OWD7PY0WXI'
    val1=get_status(dist1)
    val2=get_status(dist2)
    HEADER='&field1={}&field2={}'.format(val1,val2)
    NEW_URL=URl+KEY+HEADER
    data=urllib.request.urlopen(NEW_URL)
    print("Distance1:",dist1,",Status1:",val1)
    print("Distance2:",dist2,",Status2:",val2)
if __name__ == '__main__':
    print("Status: Occupied-1 , Vacant-0 , Not sure-2")
    thingspeak_post()

