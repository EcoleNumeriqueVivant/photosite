from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_IMG = os.path.join(BASE_DIR, "mixcat/static/mixcat/img")



def catpict(request):
    images = os.listdir(STATIC_IMG)
    image = images[0]
    print('jkhids')
    return render(request, 'mixcat/mixcat.html', {'catpict': image})
