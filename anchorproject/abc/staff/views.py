from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import StaffProfile
from django.contrib import messages, auth


def staff(request):
    
    
    # staff = get_object_or_404(StaffProfile, pk = True)        
    # context = {
    #     'staff':staff            
    # }
    return render (request,'staff/index.html')

   