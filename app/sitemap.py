from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app.models import Book


class StaticViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'quotes', 'privacy-policy', 'terms-conditions']

    def location(self, item):
        return reverse(item)


class BookSitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Book.objects.all()

    def location(self, obj):
        return reverse('details', args=[obj.id, obj.slug])
