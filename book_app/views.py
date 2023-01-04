from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
# Create your views here.
from .models import Book, Author


def show_all_books(request):
    books = Book.objects.annotate(
        true_bool=Value(True),
        new_budget=F('rating') + 10,
    )
    return render(request, 'book_app/all_books.html', {
        'books': books
    })


def show_one_book(request, slug_book: str):
    book = get_object_or_404(Book, slug=slug_book)
    return render(request, 'book_app/one_book.html', {
        'book': book
    })


def show_all_authors(request):
    authors = Author.objects.all()
    return render(request, 'book_app/all_authors.html', {
        'authors': authors
    })

def show_one_authors(request, name: str):
    author = Author.objects.get(first_name = f'{name}')
    return render(request, 'book_app/one_author.html', {
        'author': author
    })