from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True, default='')
    phone = models.IntegerField(null=True, blank=True, default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.first_name + " " + self.last_name