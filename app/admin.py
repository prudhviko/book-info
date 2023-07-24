from django.contrib import admin
from .models import Book, Category, Quote

admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(Category)
