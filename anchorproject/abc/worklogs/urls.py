from django.urls import path
from . import views

urlpatterns = [
    path('', views.loger,name='logs')
]