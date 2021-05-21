from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(requests):
    return HttpResponse('This is my first app1')