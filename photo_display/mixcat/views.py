import os
import random
from django.shortcuts import render
from mixcat import static
# from django import static
# from django.conf import settings

# from .models import Picture


def index(request):
    return render(request, 'mixcat/index.html', {})

def catpict(request):
    return render(request, 'mixcat/catimg.html', {})
