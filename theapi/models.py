from django.db import models

# Create your models here.
class Country(models.Model):
    Name = models.CharField(max_length=200,unique=True)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()
    def __str__(self):
        return self.Name

class State(models.Model):
    Country= models.ForeignKey(Country,related_name='State',on_delete = models.CASCADE)
    Name = models.CharField(max_length=200,unique=True)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()
    def __str__(self):
        return self.Name

class City(models.Model):
    State=models.ForeignKey(State,related_name='City',on_delete = models.CASCADE)
    Country= models.ForeignKey(Country,related_name='City',on_delete = models.CASCADE)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()
    PinCode=models.CharField(max_length=200)


class Town(models.Model):
    State=models.ForeignKey(State,related_name='Town',on_delete = models.CASCADE)
    Country= models.ForeignKey(Country,on_delete = models.CASCADE)
    Description= models.TextField()
    Population = models.IntegerField()
    GDP = models.FloatField()
    PinCode=models.CharField(max_length=200)

class Person(models.Model):
    Name= models.CharField(max_length=200)
    Town=models.ForeignKey(Town,related_name='PTown',on_delete=models.CASCADE)
    City=models.ForeignKey(City,related_name='Pcity',on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
