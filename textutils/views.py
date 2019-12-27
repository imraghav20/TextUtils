#I have created this file- Abhishek
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def removepunc(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    print (djtext)
    #analyse the text
    return HttpResponse('''<h1>remove punctuation</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

def capfirst(request):
    return HttpResponse('''<h1>capatalise first</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

def newlineremove(request):
    return HttpResponse('''<h1>remove new line</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

def spaceremove(request):
    return HttpResponse('''<h1>remove space</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button> ''')

def charcount(request):
    return HttpResponse('''<h1>count characters</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')




