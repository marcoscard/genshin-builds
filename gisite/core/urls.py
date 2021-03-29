from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('builds/', views.builds, name='builds'),
    re_path('builds/new-build', views.build_form, name='build_form'),
]