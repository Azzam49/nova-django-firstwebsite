from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # HttpReponse :
        # allows our view function to return HTTP Reponse to the user
        # HttpResponse : serves as our Template, it return HTML in simple form
        # HttpResponse cannot return an html file
    # return HttpResponse('<h1 style="color: red;">Hello World</h1> <h2>Bye</h2>')

    # render :
        # allows our view function to return HTTP Reponse to the user
        # But the difference, that render can help us to return an whole HTML file as response
        # render is used here to return home.html for the user.
            # home.html is created at : myapp/templates/myapp/home.htm
    # return render(request, 'home.html', {}) # Error :  TemplateDoesNotExist at /home/ home.html
    return render(request, 'myapp/home.html', {})