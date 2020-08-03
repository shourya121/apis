# apis
    path('countrylist/', views.CountryList.as_view()), # get and post api for countries
    path('countrylist/<int:id>/',views.Country_List), # put,delete,get api for particular country
    path('Statelist/', views.StateList.as_view()), # get and post api for states
    path('Statelist/<int:id>/',views.State_List), # put,delete,get api for particular state
    path('citylist/', views.CityList.as_view()),# get and post api for cities
    path('citylist/<int:id>/',views.City_List),  # put,delete,get api for particular city
    path('townlist/', views.TownList.as_view()), # get and post api for town
    path('townlist/<int:id>/',views.Town_List), # put,delete,get api for particular town
    path('person/', views.PersonList.as_view()), # get and post api for person
    path('person/<int:id>/',views.Person_List), # put,delete,get api for particular person
    path('personlist/', views.personslist.as_view()), #displays all country,town,city and state of the person(pagination included)
    path('addcities/', views.add.as_view()), #api to add cities in states of a country
