from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Editorial(models.Model):
    name = models.CharField('Name', max_length=255, blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)
class Author(models.Model):
    full_name = models.CharField('Full Name', max_length=255, blank=False, default=None)
    nationality = models.CharField('Nationality', max_length=255, blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.full_name)

class Book(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3000)])
    title = models.CharField('Title', max_length=255)
    author = models.ForeignKey(Author,
        related_name='books',
        related_query_name='book',
        on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial,
        related_name='editorials',
        related_query_name='editorial',
        on_delete=models.CASCADE)
    is_available = models.BooleanField('is_available', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)