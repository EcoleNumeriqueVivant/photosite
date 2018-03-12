from django.shortcuts import render

def catpict(request):
    return render(request, 'mixcat/index.html', {})
