import requests

NAME = "lamp2"
DEVICE_TYPE = "Lamp"
DEVICE_ID = "1234"
state = "off"

def lampget():
    data = {
        "id": DEVICE_ID,
        "name": NAME,
        "state": state
    }
    return data

#Para testar, no set podemos simplesmente mudar o valor da variavel state
def lampset():
    return "OK"
