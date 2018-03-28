from django.shortcuts import render
import os
import random
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_IMG = os.path.join(BASE_DIR, "mixcat/static/mixcat/img")



def catpict(request):
    images = os.listdir(STATIC_IMG)
    image = random.choice(images)
    return render(request, 'mixcat/mixcat.html', {'imagechat': image})
