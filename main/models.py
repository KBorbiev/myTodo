from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.DateTimeField()
    date = models.DateField(auto_now_add=True)
