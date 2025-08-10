from django.db import models
from django.utils import timezone

# Create your models here.
class characters(models.Model):
    sex_choice = [
        ('M', 'Male'),
        ('F','Female'),
        ('O', 'Other'),
    ]

    skin_choices = [
        ("D",'Dark'),
        ('P','Pale'),
        ('B','Brownish'),
     ]
    
    m_st=[
        ('M','Married'),
        ('S','Single'),
    ]
    
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=15)
    sex = models.CharField(max_length=1, choices= sex_choice)
    height = models.IntegerField()
    weight = models.IntegerField()
    location = models.CharField(max_length=120)
    skin = models.CharField( choices=skin_choices, max_length=50)
    Marriage_status = models.CharField(choices=m_st, max_length=2)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    createdtime = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return self.name
    