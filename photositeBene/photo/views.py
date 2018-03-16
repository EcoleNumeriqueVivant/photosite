
from django.http import HttpResponse
import random
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_PHOTO = os.path.join(BASE_DIR, 'photo')
STATIC_IMG = os.path.join(STATIC_PHOTO, 'static/pictures')

def photo(request):
    db = open(STATIC_PHOTO + '/db.csv', 'r+')
    images = os.listdir(STATIC_IMG)
    already_displayed_images = db.readlines()
    images = list(set(images) - set(already_displayed_images)) 
    if images:
        random.shuffle(images)
        image = images[0]
        db.write(image + "\n")
        return HttpResponse("<img src=\"/static/pictures/"+ image + "\" alt=\"A random image\"/>")
    else:
        return HttpResponse("no images")
    # return HttpResponse("<img src=\"/static/pictures/chat"+str(random.randint(0, 9)+1).zfill(2)+".jpg\" alt=\"A random image\"/>")
