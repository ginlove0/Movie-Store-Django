# Generated by Django 2.1.2 on 2019-05-25 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='movies',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movie.Movie', unique=True),
        ),
    ]
