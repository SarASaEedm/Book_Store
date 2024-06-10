from django.urls import path
from track.views import tracks_index
urlpatterns = [

   path('index', tracks_index, name='tracks.index'),

]