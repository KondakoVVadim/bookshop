# Generated by Django 4.1.4 on 2023-01-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_app", "0008_heroes_book_heroes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="heroes",
            name="last_name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
