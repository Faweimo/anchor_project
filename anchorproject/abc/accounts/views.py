from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from .forms import LoginForm, UserNewForm, ExtendUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from staff.models import StaffProfile
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




def logins(request):
    
    if request.method == 'POST':
       
        staff_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        
        
        
        
        user = auth.authenticate(staff_form=staff_form,username=username, password=password)

        if user is not None:
            
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('staff')


        else:
            

            messages.error(request,'Invalid staff ID and password')
            return redirect('login')

        
    else:
        staff_form = LoginForm()
        context = {
            'staff_form':staff_form
        }    
  
    return render(request, 'registration/login.html',context)


def logouts(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('login')    