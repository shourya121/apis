from rest_framework import serializers
from .models import Country,State,Person,City,Town
from rest_framework.serializers import SerializerMethodField

class CountrySerializer(serializers.ModelSerializer):
    class Meta():
        model=Country
        fields=('id','Name','Description','GDP','Population')


class StateSerializer(serializers.ModelSerializer):

    class Meta():
        model=State
        fields=('id','Country','Name','Description','GDP','Population')

class CitySerializer(serializers.ModelSerializer):

    class Meta():
        model=City
        fields=('id','State','Country','Description','GDP','Population','PinCode')

class TownSerializer(serializers.ModelSerializer):

    class Meta():
        model=Town
        fields=('id','State','Country','Description','GDP','Population','PinCode')

class PersonSerializer(serializers.ModelSerializer):
    class Meta():
        model=Person
        fields=('id','Name','City','Town')

class personlistserializer(serializers.ModelSerializer):
     class Meta:
        model =Person
        fields = '__all__'
        depth=2


class addcities(serializers.ModelSerializer):
    State = StateSerializer(many=True)
    City=CitySerializer(many=True)
    class Meta:
        model = Country
        fields = ('id','Name','Description','GDP','Population','State','City')
