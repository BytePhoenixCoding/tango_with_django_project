# Generated by Django 4.1.6 on 2023-02-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rango", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="likes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="category",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
