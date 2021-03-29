import requests
from yeelight import Bulb

NAME = "yeelight"
DEVICE_TYPE = "Lamp"
DEVICE_ID = "5678"

bulb = Bulb("192.168.31.171")

def lampget():
    data = {
        "id": DEVICE_ID,
        "name": NAME,
        "state": str(bulb.get_properties()["power"])
    }
    return data

def lampset():
    return bulb.toggle().capitalize()
