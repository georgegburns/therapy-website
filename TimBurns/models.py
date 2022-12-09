from django.db import models

# Create your models here.

        
class Therapies(models.Model):
    
    Therapy = models.CharField(('Therapy'), max_length=100)
    
    def __str__(self):
        name = f'{self.Therapy}'
        return name
    
    class Meta:
        verbose_name= 'Therapy'


class Prices(models.Model):
    
    Type_Choices = [('Online', 'Online'), ('In Person','In Person')]
    
    Therapy = models.ForeignKey(Therapies, verbose_name=("Therapy"), on_delete=models.CASCADE)
    Online = models.DecimalField(('Online Price'), decimal_places=2, max_digits=4,)
    In_Person = models.DecimalField(('In Person Price'), decimal_places=2, max_digits=4,)
    
    def __str__(self):
        name = f'{self.Therapy} Prices'
        return name
    
    class Meta:
        verbose_name = 'Price'    
        

class Message(models.Model): 
    
    Name = models.CharField(('Name'),max_length=25)
    Email = models.EmailField(('Email'))
    Therapy = models.ForeignKey(Therapies, verbose_name=("Therapy"), on_delete=models.CASCADE)
    Type = models.CharField(('Type'), max_length=100, choices=Prices.Type_Choices)
    Message = models.CharField(('Message'),max_length=1000)
    Date = models.DateField(("Date"), auto_now_add=True)
    
    
    def __str__(self):
        name = f'{self.Name} - {self.Therapy} - {self.Type}'
        return name
    
    class Meta:
        verbose_name= 'Message'