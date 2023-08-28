from django.contrib import admin
from .models import Book, Author, Quote, Category

admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Category)
