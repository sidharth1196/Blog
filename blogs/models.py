from django.db import models
from users.models import Author
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
