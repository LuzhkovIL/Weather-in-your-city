import requests
from django.shortcuts import render

def index(request):
    appid = '47c36fb73fccd6ff5ea9cf020919466d'
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'inco': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

    return render(request, 'templates_weather/index.html', context)
