from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class Tweep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField()
    tweeps = models.TextField(max_length=600)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tweep_id': self.id})