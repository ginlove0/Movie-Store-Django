# Generated by Django 2.1.2 on 2019-03-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20190327_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='type',
        ),
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.ManyToManyField(null=True, to='movie.Type'),
        ),
    ]
