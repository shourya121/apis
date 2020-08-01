from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length=200,unique=True)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()

class State(models.Model):
    id =models.IntegerField(primary_key = True)
    Country= models.ForeignKey(Country,on_delete = models.CASCADE)
    Name = models.CharField(max_length=200,unique=True)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()

class City(models.Model):
    id =models.IntegerField(primary_key = True)
    State=models.ForeignKey(State,on_delete = models.CASCADE)
    Country= models.ForeignKey(Country,on_delete = models.CASCADE)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()
    PinCode=models.CharField(max_length=200)

class Town(models.Model):
    id =models.IntegerField(primary_key = True)
    State=models.ForeignKey(State,on_delete = models.CASCADE)
    Country= models.ForeignKey(Country,on_delete = models.CASCADE)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()
    PinCode=models.CharField(max_length=200)

class Person(models.Model):
    id=models.IntegerField(primary_key = True)
    Name= models.CharField(max_length=200)
