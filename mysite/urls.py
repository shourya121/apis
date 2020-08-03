"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from theapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('countrylist/', views.CountryList.as_view()),
    path('countrylist/<int:id>/',views.Country_List),
    path('Statelist/', views.StateList.as_view()),
    path('Statelist/<int:id>/',views.State_List),
    path('citylist/', views.CityList.as_view()),
    path('citylist/<int:id>/',views.City_List),
    path('townlist/', views.TownList.as_view()),
    path('townlist/<int:id>/',views.Town_List),
    path('person/', views.PersonList.as_view()),
    path('person/<int:id>/',views.Person_List),
    path('personlist/', views.personslist.as_view()),
    path('addcities/', views.add.as_view()),
]
