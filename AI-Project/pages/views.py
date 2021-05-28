from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .platform.main import *
from django.core.files.storage import FileSystemStorage
from .weatherapi import getWeather

reset = True
off = True

tempStatus = None
minTemp = None
maxTemp = None

def error404(request, exception):
    return redirect('home')
def error500(request):
    return redirect('home')
def error403(request, exception):
    return redirect('home')
def error400(request, exception):
    return redirect('home')    


def homePageView(request,id=None):
    f = open("env.settings", "r")
    data = f.read()
    content = data.split(",")
    home = content[0]
    city = content[1]
    global reset
    global tempStatus
    global minTemp
    global maxTemp
    if reset:
        start()
        weather = getWeather(city)
        if weather:
            tempStatus = weather[0]
            minTemp = weather[1]
            maxTemp = weather[2]
        reset = False
    devices = getDevices()
    if id == 0:
        global off
        print(off)
        if off:
            turnAllOff()
            off = False
        else:
            turnAllOn()
            off = True
        devices = loadStatus()
        reset = True
    if id != None and id > 0:
        setSpecificDevice(id)
        devices = loadStatus()
    if request.method == 'POST':
        if request.POST['action'] == 'upload':
            uploaded_file = request.FILES['document']  
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            reset = True
            return redirect('/')
        if request.POST['action'] == 'settings':
            value1 = request.POST.get('home_name') or "Smart Home"
            value2 = request.POST.get('city_name') or "Lisbon"
            f = open("env.settings", "w")
            f.write(str(value1) + "," + str(value2))
            f.close()
            reset = True
            return redirect('/')
    return render(request=request, template_name='index.html', context={"devices": devices, "data":home, "city":city, "maxTemp":maxTemp, "minTemp":minTemp, "weather":tempStatus})


