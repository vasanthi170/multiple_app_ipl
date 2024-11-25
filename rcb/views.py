from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore

def virat(request):
    return HttpResponse('<h1> <marcque>Ee saala cup Namde!!</marcque> </h1>')
