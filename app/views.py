from django.shortcuts import render
from django.http import request
from .models import Book
from django.utils.text import slugify


def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'home.html', context)


def quotes(request):
    return render(request, 'quotes.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contactus.html')


def single(request, slug):
    book = Book.objects.get(slug=slug)
    context = {'book': book}
    return render(request, 'single.html', context)


def privacypolicy(request):
    return render(request, 'privacy-policy.html')


def termsconditions(request):
    return render(request, 'terms-conditions.html')
