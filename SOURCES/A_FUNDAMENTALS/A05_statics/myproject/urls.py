
#from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from .views import home

urlpatterns = [
    path('', home, name='myproject_home'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico') ),
    path('milligram/', include('milligram.urls') ),
]


