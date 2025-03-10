from django.urls import path
from .views import load_map

urlpatterns = [
    path('', load_map, name='home'),  # Now "/" will load the map
    path('map/', load_map, name='load_map'),
]
