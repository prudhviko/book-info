from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('quotes/', views.quotes, name='quotes'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/<slug:slug>/', views.single, name='details')
]
