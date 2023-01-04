from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    author_email = models.EmailField(default='govnariki@gmail.com')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    title = models.CharField(max_length=70)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    is_best_selling = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)
    slug = models.SlugField(default='', null=False)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    author_contact = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)

    def get_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} - {self.rating}%'

# python manage.py shell_plus --print-sql
# from book_app.models import Book
