from django.urls import path
from Chat.views import home, room, checkview, send

urlpatterns = [
    path('', home, name='home'),
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send')
]
