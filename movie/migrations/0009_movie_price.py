# Generated by Django 2.1.2 on 2019-04-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_movie_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
