from django.db import models

class login(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    mobile = models.CharField(max_length=12)

    def  __str__(self):
        return self.name



class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):


        return self.name



class registration(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(max_length=3)
    email = models.CharField(max_length=100)
    def __str__(self):

        return self.name