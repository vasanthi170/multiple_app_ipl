from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore

def someone(request):
    return HttpResponse('<h1>It was Executed </h1>')
