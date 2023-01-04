# Generated by Django 4.1.4 on 2023-01-04 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_app", "0004_author_alter_book_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author_contact",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="book_app.author",
            ),
        ),
    ]