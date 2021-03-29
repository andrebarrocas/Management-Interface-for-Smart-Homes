from django.urls import path
from .views import homePageView

urlpatterns = [
    path('<int:id>', homePageView, name='home')
]