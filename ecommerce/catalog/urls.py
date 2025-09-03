from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list, name='main_menu') ,
    path('detail/<int:pk>/' , views.product_detail , name='product_detail'),
]