import os
import random
from django.shortcuts import render
from django import static
from django.conf import settings

# from .models import Picture
register = 

def index(request):
    return render(request, 'mixcat/index.html', {})

def catpict(request):
    return render(request, 'mixcat/catimg.html', {})

def random_image(request):
    pick = random.choice()
