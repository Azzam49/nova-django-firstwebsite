from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):


    # Steps:
        # (in future) 1 - get data from database

    # 2 - give data to html
    context = {
        "name": "Alice",
        "age": 30,
        "phone": "0123456",
        "address": "KL",

        "subjects": ["English", "Math", "Coding", "History", "Geo", "Art", "Sport"],

        "books": [
            {
                "title": 'The Python Cookbook',
                "author": "David Beazley",
                "pages": 500,
            },
            {
                "title": "Automate the Boring Stuff",
                "author": "Al Sweigart",
                "pages": 400,
            },
            {
                'title': 'Fluent Python',
                'author': 'Luciano Ramalho',
                'pages': 800,
            },
        ],
    }
    # 3 (go to home.html) - use data on html


    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html', {})

def contact(request):
    return render(request, 'myapp/contact.html', {})