from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'lending/index.html')

def lending(request):
    return render(request,"lending/Lending.html")
