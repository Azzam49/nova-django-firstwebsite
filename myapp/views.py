from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime, timedelta

def home(request):


    # Steps:
        # (in future) 1 - get data from database

    print(f"\ndatetime.now() : {datetime.now()}\n")

    # 2 - give data to html
    context = {
        "nonexists": "",
        "nonexists_none": None,
        # "joined_at": datetime.now(),# joined_at will be the time now, when you start your website
        "joined_at": datetime.now() - timedelta(days=2),
        "name": "Alice",
        "age": 30,
        "phone": "0123456",
        "address": "KL",
        "is_graduated": True,

        "subjects": ["English", "Math", "Coding", "History", "Geo", "Art", "Sport"],

        "books": [
            {
                "title": 'The Python Cookbook',
                "author": "David Beazley",
                "pages": 500,
                "read": False,
            },
            {
                "title": "Automate the Boring Stuff",
                "author": "Al Sweigart",
                "pages": 400,
                "read": True,
            },
            {
                'title': 'Fluent Python',
                'author': 'Luciano Ramalho',
                'pages': 800,
                "read": False,
            },
        ],
    }
    # 3 (go to home.html) - use data on html


    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html', {})

def contact(request):
    return render(request, 'myapp/contact.html', {})