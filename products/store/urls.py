from django.urls import path
from . import views
from .views import view_schema, add_product

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('schema/', view_schema, name='view_schema'),
    path('add/', add_product, name='add_product'),
]
