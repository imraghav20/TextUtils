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
    charcount = request.GET.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed extra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        k = 0
        for i in djtext:
            k+=1
        params = {'purpose':'Counted characters', 'analyzed_text': 'Number of characters in entered text are ' + str(k)}
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




