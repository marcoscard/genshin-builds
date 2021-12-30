from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('builds/', views.builds, name='builds'),
    path('builds/new-build/', views.build_form, name='build_form'),
    path('builds/<slug:slug>/', views.detailed_build, name='detailed_build'),
]