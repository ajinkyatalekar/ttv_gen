from django.urls import path
from . import views


urlpatterns = [
    path('select_posts', views.select_posts, name='select_posts'),
    path('gen_video', views.gen_video, name='gen_video'),
]