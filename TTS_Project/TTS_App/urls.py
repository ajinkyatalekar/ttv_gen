from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('logged_in_home', views.logged_in_home, name="logged_in_home")
]