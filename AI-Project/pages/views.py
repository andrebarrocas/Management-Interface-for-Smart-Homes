from django.shortcuts import render
from django.http import HttpResponse
from .platform.main import *


def homePageView(request):
    light = "Off"
    t = "Lamp"
    print(getDevices()[0]["id"])
    print(setSpecificDevice(5678))
    print(setSpecificDevice(1234))
    print(getSpecificDevice(5678))
    return render(request=request, template_name='index.html', context={"light": light, "type":t})
