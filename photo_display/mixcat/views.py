from django.shortcuts import render
# from .models import Picture

def index(request):
    return render(request, 'mixcat/index.html', {})

def catpict(request):
    return render(request, 'mixcat/catimg.html', {})
