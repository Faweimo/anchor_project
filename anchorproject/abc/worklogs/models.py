from django.db import models
from datetime import datetime
from django.utils.timezone import timezone
import pytz
from .utils import work_id
# Create your models here.
class Logger(models.Model):
    work_id = models.CharField(default=work_id(),max_length=20)
    full_name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True,null=True)
    department = models.CharField(max_length=200,blank=True,null=True)
    team_leader = models.CharField(max_length=200,blank=True,null=True)
    work_title = models.CharField(max_length=200,blank=True,null=True)
    clock_in = models.DateTimeField(datetime.now(),blank=True,null=True)
    user_id = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.full_name

