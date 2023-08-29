from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from tinymce.widgets import TinyMCE


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = HTMLField()
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}{self.slug}/'

    class Meta:
        ordering = ['-created_at']


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuotesCategory(models.Model):
    categoryName = models.CharField(max_length=256)

    def __str__(self):
        return self.categoryName


class Quote(models.Model):
    image = models.ImageField(upload_to='quotes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        QuotesCategory, on_delete=models.CASCADE, default='Motivational', null=True)

    class Meta:
        ordering = ['-created_at']
