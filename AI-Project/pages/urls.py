from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('<int:id>', homePageView, name='home')
]