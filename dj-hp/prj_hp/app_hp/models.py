from django.db import models

# Create your models here.
class Langinf(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=2)
    link = models.URLField()
    image = models.ImageField(null=True, upload_to='images/')
