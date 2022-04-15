import django
from django.shortcuts import render
from django.shortcuts import HttpResponse


def about (request):
    # return HttpResponse('hello word')
    return render(request , 'about.html')

def home (request):
    # return HttpResponse('hello word')
    return render(request , 'Home.html')
