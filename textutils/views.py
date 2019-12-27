#I have created this file- Abhishek
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is your first page.</h1>")
