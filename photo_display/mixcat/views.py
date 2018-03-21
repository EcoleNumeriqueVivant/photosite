from django.shortcuts import render

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_IMG = os.path.join(BASE_DIR, "mixcat/static/img")
# images = os.listdir(STATIC_IMG)
# from .models import Picture


def catpict(request):
    images = []
    return render(request, 'mixcat/mixcat.html', {"images": images})
