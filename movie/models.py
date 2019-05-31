from django.db import models
import datetime
from django.core.exceptions import ValidationError

# Create your models here.

# define model type for movie
def movie_image_path(instance, filename):
    title = instance.name
    return 'movies/%s-%s' % (title, filename)

def validate_image(value):
    if value.width != 1920 and value.height != 1080:
        raise ValidationError("The image should be in HD format (1920x1080)")
    else:
        return value

class Type(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


# define movie model
class Movie(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    in_stock = models.IntegerField(default=0, blank=False, null=False)
    datetime_release = models.DateField(null=True, blank=True)
    date_in_database = models.DateField(default=datetime.date.today)
    movie_images = models.ImageField(upload_to=movie_image_path, default=None, null=True, blank=True,validators=[validate_image])
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    type = models.ManyToManyField(Type, blank=True)


    def __str__(self):
        return self.name