from django.contrib import admin
from django.urls import include, path
from htmlwebsite import views

app_name='htmlwebsite'

urlpatterns = [

    path('', views.home, name='home'),

    path('signin', views.signin, name='signin'),

    path('vote', views.vote, name='vote'),


]