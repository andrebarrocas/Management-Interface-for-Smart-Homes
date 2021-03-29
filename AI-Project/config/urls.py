# config/urls.py
from django.contrib import admin
from django.urls import path, include # new
handler404 = 'pages.views.error404'
handler403 = 'pages.views.error403'
handler400 = 'pages.views.error400'
handler500 = 'pages.views.error500'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
]