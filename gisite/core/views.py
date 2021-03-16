from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': "Home",
    }
    return render(request, 'core/index.html', context=context)