from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from books.models import Book


def landing_page(request):
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-publishing_date')[:1]

    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Landing page'
    }

    return render(request, 'books/landing.html', context)



def books_list(request):
    list_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating'),
    )

    context = {
        'books': list_books,
        'page_title': 'Dashboard'
    }

    return render(request, 'books/list.html', context)


def details(request, slug):
    book = get_object_or_404(
        Book.objects.annotate(avg_rating=Avg('reviews__rating')),
        slug=slug
    )

    context = {
        'book': book,
        'page_title': f'{book.title} details'
    }

    return render(request, 'books/details.html', context)
