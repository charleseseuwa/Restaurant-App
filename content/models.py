from django.db import models

# Create your models here

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):

    SUBJECT_CHOICES = (
        ('select', 'select1'),
        ('select', 'select3'),
        ('select', 'select4')
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=6)
    
    def __str__(self):
        return self.name



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email






class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    

    def __str__(self):
        return self.name