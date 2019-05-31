from django.db import models
from movie.models import Movie
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

def validate_status(value):
    if value == 'process' or value == 'cancel' or value == 'sucess':
        raise ValidationError(('status can only be process, cancel or success'))


class Shipment(models.Model):
    address = models.CharField(max_length=255, null=True)
    order_user_name = models.CharField(max_length=255, null=True)
    date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.address


class MovieStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name





# Create your models here.
class Order(models.Model):

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_make_order = models.DateField(default=datetime.date.today)
    status = models.ForeignKey(MovieStatus, on_delete=models.SET_NULL, null=True, blank=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return self.shipment.order_user_name



class MovieOrder(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number_of_movie = models.IntegerField(default=1)