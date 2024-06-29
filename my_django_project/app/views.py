# blog/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'about.html')
