from django.urls import path
from . import views



urlpatterns = [
    path('login', views.logins, name= 'login'),
    path('logout',views.logouts,name='logout'),
    path('signup/',views.register, name= 'signup'),
]