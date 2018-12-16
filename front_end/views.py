from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, template_name='front_end/index.html', context={'status' : 'ok'})

def navbar(request):
    return render(request, template_name='front_end/navbar-demo.html', context={'status' : 'ok'})

def dashboard(request):
    return render(request, template_name='front_end/dashboard.html', context={'status' : 'ok'})

def element(request):
    return render(request, template_name='front_end/element.html', context={'status' : 'ok'})

def tables(request):
    return render(request, template_name='front_end/tables.html', context={'status' : 'ok'})
