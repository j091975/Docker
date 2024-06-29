from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('image-links/', views.image_links, name='image_links'),
    path('wiki/', views.wiki, name='wiki'),
    path('products/', views.product_list, name='product_list'),
    path('schema/', views.view_schema, name='view_schema'),
    path('add/', views.add_product, name='add_product'),
]
 