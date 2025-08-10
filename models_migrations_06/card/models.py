from django.db import models
from django.utils import timezone

# Create your models here.
class card_varities(models.Model):
    CARD_TYPES = [
        ('MC', 'Marage Card'),
        ('RC', 'Reception Card'),
        ('DC', 'Death Card'),
        ('BC', 'Birthday Card'),
        ('BS', 'Baby Shower Card'),
    ]

    name = models.CharField(max_length= 50)
    image = models.ImageField(upload_to= 'card/')
    date_addded= models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=CARD_TYPES)
    description = models.TextField('')
    cost = models.IntegerField()

    def __str__(self):
        return self.name

    
