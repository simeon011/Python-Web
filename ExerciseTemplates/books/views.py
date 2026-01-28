from django.db.models import Avg, Q
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookForm, CreateBookForm, EditBookForm, DeleteBookForm, BookSearchForm
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
    search_form = BookSearchForm(request.GET or None)

    list_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating'),
    )

    if request.GET:
        if search_form.is_valid():
            list_books = list_books.filter(Q(title__icontains=search_form.cleaned_data['query'])
                                           |
                                           Q(description__icontains=search_form.cleaned_data['query']))

    context = {
        'books': list_books,
        'page_title': 'Dashboard',
        'search_form': search_form,

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


def book_create(request):
    form = CreateBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("books:home")

    context = {
        "form": form,
    }

    return render(request, 'books/create.html', context)


def edit_book(request, pk: int):
    book = Book.objects.get(pk=pk)
    form = EditBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("books:home")

    context = {
        "form": form,
    }

    return render(request, 'books/edit.html', context)


def delete_book(request, pk: int):
    book = Book.objects.get(pk=pk)
    form = DeleteBookForm(request.POST or None, instance=book)
    if form.is_valid():
        book.delete()
        return redirect("books:home")

    context = {
        "form": form,
    }

    return render(request, 'books/delete.html', context)
