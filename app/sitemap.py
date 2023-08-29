from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app.models import Book


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home', 'about', 'quotes', 'privacy-policy', 'terms-conditions']

    def location(self, item):
        return reverse(item)


class BookSitemap(Sitemap):
    def item(self):
        return Book.objects.all()
