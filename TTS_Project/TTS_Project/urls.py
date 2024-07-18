from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TTS_App.urls')),
    path('app/', include('RedditTTS.urls')),

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('Authenticator.urls')),
]
