#I have created this file- Abhishek
from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1>HOME</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/removepunc/"> RemovePunctuation </a></button>
<br> <button type="button"> <a href="http://127.0.0.1:8000/capitalizefirst/"> CapitaliseFirst </a></button>
<br> <button type="button"> <a href="http://127.0.0.1:8000/newlineremove/"> NewLineRemove </a></button>
<br> <button type="button"> <a href="http://127.0.0.1:8000/spaceremove/"> SpaceRemove </a></button>
<br> <button type="button"> <a href="http://127.0.0.1:8000/charcount/"> CountCharacters </a></button>''')

def removepunc(request):
    return HttpResponse('''<h1>remove punctuation</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

def capfirst(request):
    return HttpResponse('''<h1>capatalise first</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

def newlineremove(request):
    return HttpResponse('''<h1>remove new line</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

def spaceremove(request):
    return HttpResponse('''<h1>remove space</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button> ''')

def charcount(request):
    return HttpResponse('''<h1>count characters</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')




