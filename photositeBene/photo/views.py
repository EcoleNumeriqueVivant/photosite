
from django.http import HttpResponse
import random


def photo(request):
    return HttpResponse("<img src=\"/static/pictures/chat"+str(random.randint(0, 9)+1).zfill(2)+".jpg\" alt=\"chat.jpg\"/>")
