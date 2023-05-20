
from django.http import HttpResponse
from django.urls import path
from .views import hi, Salut


urlpatterns = [
    path('hello/', lambda req: HttpResponse("<h1>Hello</h1>") ),
    path('hello/<str:who>', lambda req, who: HttpResponse(f"<h1>Hello {who}</h1>")),
    path('hi', hi ),
    path('hi/<str:who>', hi ),
    path('salut', Salut.as_view() ),
]
