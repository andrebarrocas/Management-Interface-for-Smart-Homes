from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .platform.main import *
from django.core.files.storage import FileSystemStorage

reset = True
off = True

def error404(request, exception):
    return redirect('home')
def error500(request):
    return redirect('home')
def error403(request, exception):
    return redirect('home')
def error400(request, exception):
    return redirect('home')    


def homePageView(request,id=None):
    global reset
    print(reset)
    if reset:
        start()
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
        return render(request=request, template_name='index.html', context={"devices": devices})
    if id != None and id > 0:
        setSpecificDevice(id)
        devices = loadStatus()
    if request.method == 'POST':
        uploaded_file = request.FILES['document']  
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        reset = True
        return redirect('/')
    return render(request=request, template_name='index.html', context={"devices": devices})


