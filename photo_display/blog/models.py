from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cat_choices = models.CharField(
     max_length=50,
        choices=(
            ('/static/pictures/chat01.jpg', 'chat01'),
            ('/static/pictures/chat02.jpg', 'chat02'),
            ('/static/pictures/chat03.jpg', 'chat03'),
            ('/static/pictures/chat04.jpg', 'chat04'),
            ('/static/pictures/chat05.jpg', 'chat05'),
            ('/static/pictures/chat06.jpg', 'chat06'),
            ('/static/pictures/chat07.jpg', 'chat07'),
            ('/static/pictures/chat08.jpg', 'chat08'),
            ('/static/pictures/chat09.jpg', 'chat09'),
            ('/static/pictures/chat10.jpg', 'chat10'),
            ),
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
