
from django.http  import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse


def home(request):
    return HttpResponseRedirect('/milligram/about')

class AboutView(TemplateView):
    template_name="milligram/about.html"

