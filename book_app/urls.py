from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_books),
    path('book/<str:slug_book>', views.show_one_book, name='book-detail'),
    path('authors/', views.Show_all_authors.as_view()),
    path('authors/<str:name>', views.show_one_authors, name='author-detail'),
    path('heroe/<str:name>', views.show_one_hero, name='hero-detail'),
]