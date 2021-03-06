# from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager
from django.utils import timezone


class Tweep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    tweeps = models.TextField(max_length=1000)
    # tags = TaggableManager()

    def __str__(self):
        return self.tweeps

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tweep_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    tweep = models.ForeignKey(Tweep, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for tweep_id: {self.tweep_id} @{self.url}"

class Comment(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=100)
    tweep = models.ForeignKey(Tweep, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for tweep_id: {self.comment_id} @{self.url}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comment_id': self.id})
