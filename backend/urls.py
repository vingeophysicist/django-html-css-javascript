from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .views import retrieve_json_data


app_name = 'backend'


urlpatterns = [
    path('', views.index, name ='indexpage'),
    path('api/<str:user_type>/', retrieve_json_data, name='retrieve_json_data')
]