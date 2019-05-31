# Generated by Django 2.1.2 on 2019-05-25 11:48

from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, null=True)),
                ('order_user_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='process', max_length=65, validators=[order.models.validate_status]),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Shipment'),
        ),
    ]
