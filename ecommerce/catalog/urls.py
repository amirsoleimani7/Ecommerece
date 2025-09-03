from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list, name='main_menu') ,
    path('detail/<int:pk>/' , views.product_detail , name='product_detail'),
    path('add/<int:product_id>/' , views.add_to_cart , name='add_to_cart') ,
    path('remove/<int:item_id>/' , views.remove_from_cart, name='remove_from_cart')  ,
    path('cart/' , views.cart_view , name='cart_view')
]