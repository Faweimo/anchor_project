from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Staff_profile
from django.contrib import messages


def staff(request):
    staffs = Staff_profile.objects.all()
    context = {
        'staffs':staffs,
        
    }
    
  
    return render (request,'staff/index.html',context)