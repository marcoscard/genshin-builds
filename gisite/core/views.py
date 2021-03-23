from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests


API_GENSHIN = "https://api.genshin.dev"

# Create your views here.
def index(request):
    context = {
        'title': "Home",
    }
    return render(request, 'core/index.html', context=context)


def builds(request):
    characters = requests.get(API_GENSHIN + "/characters/")
    characters = characters.json()
    context = {
        'title': "Builds",
        'characters': characters,
        'url_api': API_GENSHIN+"/characters",
    }
    return render(request, 'core/builds.html', context=context)