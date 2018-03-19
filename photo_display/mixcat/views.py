import os
import random
from django.shortcuts import render
from mixcat import static

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_IMG = os.path.join(BASE_DIR, "mixcat/static/img")
images = os.listdir(STATIC_IMG)
# from .models import Picture


def index(request):
    return render(request, 'mixcat/index.html', {})

def catpict(request):
    return render(request, 'mixcat/catimg.html', {})
