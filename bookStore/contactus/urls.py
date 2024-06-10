from django.urls import path
from contactus.views import (contact)


urlpatterns = [
    path('index',contact, name='contactFun')
]

