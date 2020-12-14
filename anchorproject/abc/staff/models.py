from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz
from .utils import staff_new_id



class Staff_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    staff_id = models.CharField(max_length=10,default=staff_new_id(),editable=True,null=True,blank=True)
    department = models.CharField(max_length=100,blank=False,null=False,default='worker')    
    display_pics = models.ImageField(default='avatar.png', null= True,blank= True,upload_to='profile pics')
    level = models.CharField(max_length=100,blank=True,null=True,default='Novice')

    
    def __str__(self):
        return str(self.user)