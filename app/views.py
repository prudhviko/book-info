from django.shortcuts import render, get_object_or_404
from django.http import request
from .models import Book, Quote
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseNotFound


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def home(request):
    queryset = Book.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(queryset, 10)
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'paginated_data': queryset})


def quotes(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 15)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context = {
        'objects': objects
    }
    return render(request, 'quotes.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contactus.html')


def details(request, post_id, slug):
    current_post = get_object_or_404(Book, id=post_id)
    previous_post = Book.objects.filter(id__lt=post_id).order_by('-id').first()
    next_post = Book.objects.filter(id__gt=post_id).order_by('id').first()

    context = {
        'post': current_post,
        'previous_post': previous_post,
        'next_post': next_post,
        'meta_title': current_post.meta_title,
        'meta_description': current_post.meta_description
    }

    return render(request, 'post.html', context)


def privacypolicy(request):
    return render(request, 'privacy-policy.html')


def termsconditions(request):
    return render(request, 'terms-conditions.html')
