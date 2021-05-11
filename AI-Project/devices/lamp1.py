import requests

NAME = "lamp1"
DEVICE_TYPE = "Lamp"
DEVICE_ID = "1234"

def lampget():
    rget = requests.get('http://localhost:8001/getstatus')
    if(rget.text == 'true'): 
        state = 'on'
    else: 
        state = 'off'
    data = {
        "id": DEVICE_ID,
        "name": NAME,
        "state": state
    }
    return data

def lampset():
    return requests.get('http://localhost:8001/setstatus').text.capitalize()
