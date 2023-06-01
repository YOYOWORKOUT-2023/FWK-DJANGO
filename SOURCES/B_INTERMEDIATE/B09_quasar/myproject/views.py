from django.shortcuts import render



# homepage
def home(request):
    return render(request, template_name='myproject/home.html')
