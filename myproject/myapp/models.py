from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200) # Titre du livre
    author = models.CharField(max_length=100) # Nom de l'auteur
    published_date = models.DateField() # Date de publication
    isbn = models.CharField(max_length=13, unique=True) # Code ISBN, unique
    def __str__(self):
        return self.title
