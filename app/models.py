from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    publication_date = models.DateField()
    description = HTMLField()
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
