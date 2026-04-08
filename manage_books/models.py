from django.db import models

# Create your models here.

class Book(models.Model):
    COVER = [
        ('Hardcover', 'Hardcover'),
        ('Paperback', 'Paperback'),
        ('E-book', 'E-book'),
        ('Audiobook', 'Audiobook'),
    ]
    Language = [
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
        ('German', 'German'),
        ('Chinese', 'Chinese'),
        ('Japanese', 'Japanese'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=20, choices=COVER)
    language = models.CharField(max_length=20)
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=100)

class Publisher(models.Model):

class Genre(models.Model):

class series(models.Model):

class Topics(models.Model):

class Category(models.Model):

class Note(models.Model):