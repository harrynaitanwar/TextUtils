# This file created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    return HttpResponse("remove punc")

def caplast(request):
    return HttpResponse("capitalize first")
def newlineremove(request):
    return HttpResponse("newlinerremove")
def spaceremove(request):
    return HttpResponse("Space remover")
def charcount(request):
    return HttpResponse("Charcount")
