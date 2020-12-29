from django import forms
from .models import Logger
import datetime


class LoggerForm(forms.ModelForm):
    # work_id = forms.IntegerField()
    # full_name = forms.CharField(max_length=200)
    # email = forms.EmailField(max_length=200)
    # department = forms.CharField(max_length=200)
    # team_leader = forms.CharField(max_length=200)
    # work_title = forms.CharField(max_length=200)
   
    # user_id = forms.IntegerField()


    class Meta:
        model = Logger
        fields = ('work_id','full_name','email','department','team_leader','work_title','clock_in','user_id')

