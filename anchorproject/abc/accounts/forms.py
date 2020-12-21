
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 

from staff.models import StaffProfile




class LoginForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ('staff_id',)



        
  