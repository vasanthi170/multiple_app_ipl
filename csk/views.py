from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse  # type: ignore

def ruturaj(request):
    return HttpResponse('<h1>Captain of csk is Ruturaj </h1>')
