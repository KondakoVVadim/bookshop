from django.contrib import admin, messages
from .models import Book, Author
from django.db.models import QuerySet

# Register your models here.
admin.site.register(Author)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'qwerty'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший')
        ]

    def queryset(self, request, qs: QuerySet):
        if self.value() == '<40':
            return qs.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return qs.filter(rating__gte=40, rating__lt=60)
        if self.value() == 'от 60 до 79':
            return qs.filter(rating__gte=60, rating__lt=80)
        if self.value() == '>=80':
            return qs.filter(rating__gte=80)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    # exclude = ['slug']
    # readonly_fields = ['author']
    list_display = ['title', 'rating', 'is_best_selling', 'rating_status', 'currency', 'author_contact']
    list_editable = ['rating', 'is_best_selling', 'currency', 'author_contact']
    ordering = ['-rating', '-title']
    list_per_page = 5
    actions = ['set_usd', 'set_eur', 'set_rub']
    search_fields = ['title']
    list_filter = ['title', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, book: Book):
        if book.rating < 50:
            return "Говно"
        if book.rating < 70:
            return "Сойдет"
        if book.rating <= 85:
            return "Зачет"
        return "Топчик"

    @admin.action(description='Установить валюту доллар')
    def set_usd(self, request, qs: QuerySet):
        qs.update(currency=Book.USD)

    @admin.action(description='Установить валюту евро')
    def set_eur(self, request, qs: QuerySet):
        qs.update(currency=Book.EUR)

    @admin.action(description='Установить валюту рубли')
    def set_rub(self, request, qs: QuerySet):
        count_updates = qs.update(currency=Book.RUB)
        self.message_user(request, 'Зрада!', messages.ERROR)
