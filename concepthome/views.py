from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {"content": "I am from index"}
    return render(request, 'concepthome/concepthome.html', context=my_dict)


def blog(request):
    my_dict = {"content": "I am from blog"}
    return render(request, 'zero_layout.html', context=my_dict)


def projects(request):
    my_dict = {"content": "I am from projects"}
    return render(request, 'zero_layout.html', context=my_dict)


def about_me(request):
    my_dict = {"content": "I am from about_me"}
    return render(request, 'zero_layout.html', context=my_dict)
