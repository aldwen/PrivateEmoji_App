from django.urls import path
from . import views

app_name = 'favemoji' #app name 用于地址引用，区分不同APP 
urlpatterns = [
    path('', views.index, name="index"),
]