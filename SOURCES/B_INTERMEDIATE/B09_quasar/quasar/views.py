from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from django.views import View




class Online(View):

    def get(self, request, *args,**kwargs):
        return render(request, 'quasar/online.html')

class Offline(View):

    def get(self, request, *args,**kwargs):
        return render(request, 'quasar/offline.html')

