
from django.http import HttpResponse
import random
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_IMG = os.path.join(BASE_DIR, 'photo/static/pictures')

def photo(request):
    images = os.listdir(STATIC_IMG)
    if images:
        random.shuffle(images)
        image = images[0]
        return HttpResponse("<img src=\"/static/pictures/"+ image + "\" alt=\"A random image\"/>")
    else:
        return HttpResponse("no images")
    # return HttpResponse("<img src=\"/static/pictures/chat"+str(random.randint(0, 9)+1).zfill(2)+".jpg\" alt=\"A random image\"/>")
