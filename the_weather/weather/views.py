# from django.shortcuts import render
# from .models import City
# from pip._vendor import requests
# from .forms import CityForm
#
#
# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b5e14c712de72bd595a37d9981170142'
#
#     cities = City.objects.all()  # return all the cities in the database
#
#     weather_data = []
#
#     for city in cities:
#         city_weather = requests.get(
#             url.format(city)).json()  # request the API data and convert the JSON to Python data types
#
#         weather = {
#             'city': city,
#             'temperature': city_weather['main']['temp'],
#             'description': city_weather['weather'][0]['description'],
#             'icon': city_weather['weather'][0]['icon']
#         }
#
#         weather_data.append(weather)  # add the data for the current city into our list
#
#     if request.method == 'POST':  # only true if form is submitted
#         form = CityForm(request.POST)  # add actual request data to form for processing
#         form.save()  # will validate and save if validate
#
#     form = CityForm()
#
#     weather_data = []
#
#     context = {'weather_data': weather_data, 'form': form}
#
#     return render(request, 'weather/index.html', context)  # returns the index.html template
#     # city = 'Las Vegas'
#     #
#     # city_weather = requests.get(
#     #     url.format(city)).json()  # request the API data and convert the JSON to Python data types
#     #
#     # weather = {
#     #     'city': city,
#     #     'temperature': city_weather['main']['temp'],
#     #     'description': city_weather['weather'][0]['description'],
#     #     'icon': city_weather['weather'][0]['icon']
#     # }
#     #
#     # context = {'weather': weather}
#     # cities = City.objects.all() #return all the cities in the database
#     #
#     # # return render(request, 'weather/index.html', context)  # returns the index.html template

from django.shortcuts import render
from pip._vendor import requests
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b5e14c712de72bd595a37d9981170142'
    cities = City.objects.all()  # return all the cities in the database

    # city = 'Las Vegas'
    #
    # city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    #
    # weather = {
    #     'city': city,
    #     'temperature': city_weather['main']['temp'],
    #     'description': city_weather['weather'][0]['description'],
    #     'icon': city_weather['weather'][0]['icon']
    # }
    # context = {'weather' : weather}
    #
    # return render(request, 'weather/index.html') #returns the index.html template

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        if form.is_valid():
            form.save()  # will validate and save if validate

    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)  # returns the index.html template
