from django.urls import path
from .views import homePageView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homePageView, name='home'),
    path('<int:id>', homePageView, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)