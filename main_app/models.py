from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone


class Tweep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweeps')
    timestamp = models.DateTimeField(default=timezone.now)
    tweeps = models.TextField(max_length=600)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tweep_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    tweep = models.ForeignKey(Tweep, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for tweep_id: {self.tweep_id} @{self.url}"
