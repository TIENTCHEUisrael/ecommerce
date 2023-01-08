from django.urls import path

from Chat.views import home

urlpatterns = [
    path('', home, name='home')
]
