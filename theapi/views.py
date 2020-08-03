from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,GenericAPIView
from .models import Country,State,City,Town,Person
from .serializers import CountrySerializer,StateSerializer,CitySerializer,TownSerializer,PersonSerializer,personlistserializer,addcities
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class CountryList(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=Country.objects.all()
            serial=CountrySerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=CountrySerializer(data=request.data)
             if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
                return Response(status=status.HTTP_201_CREATED)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Country_List(request, id):

    try:
        country = Country.objects.get(id=id)
    except Country.DoesNotExist:
        return Response("Country does not exists!",status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response("Country deleted",status=status.HTTP_204_NO_CONTENT)

class StateList(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=State.objects.all()
            serial=StateSerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=StateSerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
                 return Response(status=status.HTTP_201_CREATED)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def State_List(request, id):

    try:
        state= State.objects.get(id=id)
    except State.DoesNotExist:
        return Response("State does not exists!",status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        state.delete()
        return Response("state deleted",status=status.HTTP_204_NO_CONTENT)

class CityList(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=City.objects.all()
            serial=CitySerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=CitySerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
                 return Response(status=status.HTTP_201_CREATED)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def City_List(request, id):
    try:
        city= City.objects.get(id=id)
    except City.DoesNotExist:
        return Response("city does not exists!",status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        city.delete()
        return Response("city deleted!",status=status.HTTP_204_NO_CONTENT)

class TownList(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=Town.objects.all()
            serial=TownSerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=TownSerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
                 return Response(status=status.HTTP_201_CREATED)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Town_List(request, id):

    try:
        town= Town.objects.get(id=id)
    except Town.DoesNotExist:
        return Response("Town does not exists!",status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TownSerializer(town)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TownSerializer(town, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        town.delete()
        return Response("town deleted",status=status.HTTP_204_NO_CONTENT)

class PersonList(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=Person.objects.all()
            serial=PersonSerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=PersonSerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()
             return Response(serializer.data)
             return Response(status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Person_List(request, id):

    try:
        person=Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response("Person does not exists",status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response("Person deleted",status=status.HTTP_204_NO_CONTENT)

class personslist(ListAPIView):

    queryset=Person.objects.all()
    serializer_class=personlistserializer
    pagination_class=PageNumberPagination

class add(ListAPIView):
    queryset=Country.objects.all()
    serializer_class=CitySerializer
    def get(self,request):
        if request.method=="GET":
            users1=Country.objects.all()
            serial=addcities(users1,many=True)
            return Response(serial.data)

    def post(self,request):
          if request.method=="POST":
            serializer = CitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
