# Generated by Django 2.1.2 on 2019-05-26 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20190526_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]