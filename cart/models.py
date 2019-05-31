from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
# Create your models here.

def calculate_total_value():
    return 0

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, default='',editable=False)

