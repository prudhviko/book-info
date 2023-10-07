from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from tinymce.widgets import TinyMCE
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True,null=True)
    description = HTMLField()
    alt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=[self.id, self.slug,])

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
    text = models.TextField()
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True,null=True)
    category = models.ForeignKey(
        QuotesCategory, on_delete=models.CASCADE, default='Motivational', null=True)  
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, default='Steve Jobs', null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
