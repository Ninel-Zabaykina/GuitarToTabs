from django.db import models


class GuitarAudio(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='audio/%Y/%m/%d')
