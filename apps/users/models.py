from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from apps.books.models import Book


class CustomUser(AbstractUser):
    birthdate = models.DateField('Birthdate', blank=True, null=True)

    REQUIRED_FIELDS = []
    def __str__(self):
        return str(self.username)
class Borrow(models.Model):
    date = models.DateTimeField(blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
class Restore(models.Model):
    date = models.DateTimeField(blank=False)
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)