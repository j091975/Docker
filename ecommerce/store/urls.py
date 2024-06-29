from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('index/', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('product_insert/', views.product_insert, name='product_insert'),
    path('add/', views.add_product, name='add_product'),
]
