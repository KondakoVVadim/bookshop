from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
# Create your views here.
from .models import Book, Author, Heroes
from django.views.generic import ListView


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


class Show_all_authors(ListView):
    template_name = 'book_app/all_authors.html'
    model = Author
    context_object_name = 'authors'


def show_one_authors(request, name: str):
    author = Author.objects.get(first_name=f'{name}')
    return render(request, 'book_app/one_author.html', {
        'author': author
    })


def show_one_hero(request, name: str):
    hero = Heroes.objects.get(first_name=f'{name}')
    return render(request, 'book_app/one_hero.html', {
        'hero': hero
    })
