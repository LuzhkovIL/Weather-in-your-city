import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = '47c36fb73fccd6ff5ea9cf020919466d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&Units Default=Metric&appid=' + appid

    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'inco': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'templates_weather/index.html', context)
