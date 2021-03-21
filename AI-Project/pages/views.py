from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    light = "Off"
    t = "Lamp"
    return render(request=request, template_name='index.html', context={"light": light, "type":t})
