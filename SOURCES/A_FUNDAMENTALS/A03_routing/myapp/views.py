from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from django.views import View


# simple callable
def hi(req: HttpRequest , who: str = ''):
    msg = f"Hi {who}" if who.isalnum() else "Hi there"
    return HttpResponse(msg)


# generic view extension

class Salut(View):

    def get(self, request, *args,**kwargs):
        return HttpResponse("Salut")

