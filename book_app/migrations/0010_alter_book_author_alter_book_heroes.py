# Generated by Django 4.1.4 on 2023-01-06 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_app", "0009_alter_heroes_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="book_app.author",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="heroes",
            field=models.ManyToManyField(related_name="jopa", to="book_app.heroes"),
        ),
    ]
