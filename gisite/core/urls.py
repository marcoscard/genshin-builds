from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('builds/', views.builds, name='builds'),
]