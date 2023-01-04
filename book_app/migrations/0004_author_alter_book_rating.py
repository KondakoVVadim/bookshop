# Generated by Django 4.1.4 on 2023-01-04 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_app", "0003_alter_book_currency"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "author_email",
                    models.EmailField(default="govnariki@gmail.com", max_length=254),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ]
            ),
        ),
    ]
