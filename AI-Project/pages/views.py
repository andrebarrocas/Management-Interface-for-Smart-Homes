from django.shortcuts import render
from django.http import HttpResponse
from .platform.main import *



def error404(request, exception):
    return redirect('home')
def error500(request):
    return redirect('home')
def error403(request, exception):
    return redirect('home')
def error400(request, exception):
    return redirect('home')          

def homePageView(request):
    light = "Off"
    t = "Lamp"
    print(getDevices()[0]["id"])
    devices = getDevices()
    print(setSpecificDevice(5678))
    print(setSpecificDevice(1234))
    print(getSpecificDevice(5678))
    return render(request=request, template_name='index.html', context={"devices": devices})
