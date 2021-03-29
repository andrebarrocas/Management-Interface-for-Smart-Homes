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

def homePageView(request,id):
    light = "Off"
    t = "Lamp"
    devices = getDevices()
    setSpecificDevice(id)
    return render(request=request, template_name='index.html', context={"devices": devices})
