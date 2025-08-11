from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # HttpReponse :
        # allows our view function to return HTTP Reponse to the user
    return HttpResponse("Hello World")