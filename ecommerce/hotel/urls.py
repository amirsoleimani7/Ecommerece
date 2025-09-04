from django.urls import path , include 
from . import views


urlpatterns = [
    path('' , views.home) , 
    path("hotel/get_GFG/", views.get_hotels, name="get_GFG"),
]