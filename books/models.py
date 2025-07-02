from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_pages = models.PositiveIntegerField()

    # the string reprentation of the model
    def __str__(self):
        return f"{self.title} by {self.author}"