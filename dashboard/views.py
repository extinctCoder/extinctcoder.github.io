from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"content": "I am from index"}
    return render(request, 'dashboard/concepthome.html', context=context)


def login(request):
    context = {"content": "I am from login"}
    return render(request, 'dashboard/login.html', context=context)


def register(request):
    context = {"content": "I am from register"}
    return render(request, 'dashboard/register.html', context=context)
