from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from .forms import BuildForm
from .models import Build

API_GENSHIN = "https://api.genshin.dev"

# Create your views here.
def index(request):
    context = {
        'title': "| Home",
    }
    return render(request, 'core/index.html', context=context)


def builds(request):
    context = {
        'title': "| Builds"
    }
    return render(request, 'core/builds.html', context=context)


def build_form(request):
    characters = requests.get(API_GENSHIN + "/characters/")
    characters = characters.json()
    if request.method == 'POST':
        form = BuildForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
        
    else:
        form = BuildForm()
    context = {
        'title': "| New Build",
        'characters': characters,
        'url_api': API_GENSHIN+"/characters",
        'form': form,
    }
    return render(request, 'core/build_form.html', context=context)


def detailed_build(request, slug):
    obj = Build.objects.get(slug=slug)
    ctx = {
        "object": obj
    }
    return render(request, "core/detailed_build.html", context=ctx)