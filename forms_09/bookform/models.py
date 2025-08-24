from django.db import models

# Create your models here.
class book(models.Model):
    cat = [
        ('YA','Young Adult'),
        ('DT', 'Documentary'),
        ('FI', 'Fiction'),
        ('RO', 'Romance'),
        ('FA', 'Fantacy'),
        ('KI', 'Kids'),
    ]
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(choices=cat)
    Published_yr = models.DateField()
    About_book = models.TextField()

    def __str__(self):
        return f'{self.bookname} - Author {self.author}'