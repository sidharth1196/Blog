from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)