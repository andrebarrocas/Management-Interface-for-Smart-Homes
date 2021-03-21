from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    # return HttpResponse('Hello, World!')
    u = ""
    return render(request=request, template_name='index.html', context={"utilizadores": u})
