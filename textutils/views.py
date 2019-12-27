#I have created this file- Abhishek
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is your first page.")
