from django.conf.urls import url
from mixcat.views import catpict
from . import views


urlpatterns = [
    url(r'^$', views.catpict),


]
