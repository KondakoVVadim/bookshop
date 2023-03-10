# Generated by Django 4.1.4 on 2023-01-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_app", "0002_book_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="currency",
            field=models.CharField(
                choices=[("EUR", "Euro"), ("USD", "Dollar"), ("RUB", "Rubles")],
                default="RUB",
                max_length=3,
            ),
        ),
    ]
