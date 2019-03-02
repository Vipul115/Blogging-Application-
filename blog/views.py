from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Vipul Rustagi',
        'title': 'Motivation',
        'content': 'First blog content',
        'date': 'August 27, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Perseverence',
        'content': 'Second blog content',
        'date': 'August 28, 2019'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})