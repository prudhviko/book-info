from django.contrib import admin
from .models import Book, Author, Quote, QuotesCategory

admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(QuotesCategory)
