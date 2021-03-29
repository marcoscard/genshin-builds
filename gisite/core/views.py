from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from .forms import BuildForm

API_GENSHIN = "https://api.genshin.dev"

# Create your views here.
def index(request):
    context = {
        'title': "Home",
    }
    return render(request, 'core/index.html', context=context)


def builds(request):
    context = {}
    return render(request, 'core/builds.html', context=context)


def build_form(request):
    characters = requests.get(API_GENSHIN + "/characters/")
    characters = characters.json()
    if request.method == 'POST':
        form = BuildForm(request.POST)
        
        if form.is_valid():
            #Atualizar no banco de dados!!
            return HttpResponseRedirect('/thanks/')
        
    else:
        form = BuildForm()
    context = {
        'title': "Builds",
        'characters': characters,
        'url_api': API_GENSHIN+"/characters",
        'form': form,
    }
    return render(request, 'core/build_form.html', context=context)