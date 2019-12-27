#I have created this file- Abhishek
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")


#def capfirst(request):
    #return HttpResponse('''<h1>capatalise first</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

#def newlineremove(request):
    #return HttpResponse('''<h1>remove new line</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')

#def spaceremove(request):
    #return HttpResponse('''<h1>remove space</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button> ''')

#def charcount(request):
    #return HttpResponse('''<h1>count characters</h1> <br> <button type="button"> <a href="http://127.0.0.1:8000/"> GoBack </a></button>''')




