from django.shortcuts import render
from django.http import HttpResponse
from .platform.main import *
from django.core.files.storage import FileSystemStorage

def error404(request, exception):
    return redirect('home')
def error500(request):
    return redirect('home')
def error403(request, exception):
    return redirect('home')
def error400(request, exception):
    return redirect('home')          

def homePageView(request,id=None):
    light = "Off"
    t = "Lamp"
    # devices = getDevices()
    # if not None:
    #     setSpecificDevice(id)
    if request.method == 'POST':
        uploaded_file = request.FILES['document']   
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request=request, template_name='index.html')#, context={"devices": devices})#,'form': form})


