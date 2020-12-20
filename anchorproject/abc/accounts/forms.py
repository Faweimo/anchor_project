from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 

from staff.models import Staff_profile

class LoginForm():
    staff_id = forms.CharField()
    class Meta:
        model = Staff_profile
        fields = ['staff_id']



# class CreateForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']

# class UserRegisterForm(UserCreationForm):
#    staff_id = forms.CharField()
   
#    department = forms.CharField()
#    level = forms.CharField()


#     class Meta:
#         model = User 
#         fields = ['username','email','first_name','password1','password2'] 



        
  