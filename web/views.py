from django.shortcuts import render

def index(requst):
    return render(requst, 'templates_weather/index.html')
