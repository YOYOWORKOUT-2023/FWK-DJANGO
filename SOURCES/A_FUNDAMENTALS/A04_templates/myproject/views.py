from django.shortcuts import render



# homepage
def home(request):
    return render(request, template_name='myproject/home.html')


def hello(request):
    return render(request, template_name='myproject/hello.html')

def about(request):
    return render(request, template_name='myproject/about.html')
