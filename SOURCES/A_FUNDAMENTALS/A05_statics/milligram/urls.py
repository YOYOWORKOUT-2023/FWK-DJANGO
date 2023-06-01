
from django.urls import path
from .views import AboutView, home


urlpatterns = [
    path('', home ),
    path('about', AboutView.as_view(), name='milligam_about' ),
]


