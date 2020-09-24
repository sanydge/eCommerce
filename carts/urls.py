from django.urls import path

from .views import (cart_home, cart_update)

app_name = 'cart'

urlpatterns = [
    path(r'^$', cart_home, name='home'),
    path(r'^update/$', cart_update, name='update'),
]
