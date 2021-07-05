from django.urls import path
from mysiteapp import views

urlpatterns = [
    path('', views.index, name='mysiteapp_index')
]