from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.sitemap import StaticViewSitemap, BookSitemap,QuotesSitemap
from django.contrib.sitemaps.views import sitemap

handler404 = 'app.views.custom_404'
sitemaps = {
    'static': StaticViewSitemap,
    'book': BookSitemap,
    'quotesitemap': QuotesSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
