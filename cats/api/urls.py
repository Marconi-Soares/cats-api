from django.urls import path 
from .views import cat_view 

urlpatterns = [path('cats/', cat_view, name='cats')]
