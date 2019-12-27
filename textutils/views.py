#I have created this file- Abhishek
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>HOME</h1>")

def removepunc(request):
    return HttpResponse("remove punctuation")

def capfirst(request):
    return HttpResponse("capatalise first")

def newlineremove(request):
    return HttpResponse("remove new line")

def spaceremove(request):
    return HttpResponse("remove space")

def charcount(request):
    return HttpResponse("count characters")




