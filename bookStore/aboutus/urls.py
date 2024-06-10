from django.urls import path
from aboutus.views import (aboutus)


urlpatterns = [
    path('index',aboutus, name='aboutusFun')
]

