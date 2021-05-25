from django.http import HttpResponse
from django.shortcuts import render
from .models import Service,Master

# Create your views here.
def homepage(requests):
    return HttpResponse('This is my first app1')

def services(request):
    services = Service.objects.all()
    return render(request,'service.html',{'services':services})

def masters(request):
    masters = Master.objects.all()
    return render(request, 'master.html',{'masters':masters})