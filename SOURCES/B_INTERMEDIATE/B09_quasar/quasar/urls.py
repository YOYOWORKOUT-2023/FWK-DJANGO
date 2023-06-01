
from django.http import HttpResponse
from django.urls import path
from .views import Online, Offline


urlpatterns = [
    path('', lambda req: HttpResponse("<h1>Hello</h1>") ),
    path('online', Online.as_view(), ),
    path('offline', Offline.as_view(), ),
]
