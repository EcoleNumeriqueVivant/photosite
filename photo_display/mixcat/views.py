from django.shortcuts import render
# from .models import Picture

def catpict(request):
    return render(request, 'mixcat/index.html', {})
