from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz
# Create your models here.

class Work_log(models.Model):
    first_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team_leader = models.CharField(max_length=200)
    clock_in = models.DateTimeField(default=datetime.datetime.now(tz=pytz.UTC),blank=False,null=False)
    work_title = models.CharField(max_length=200,blank=False,null=False)
    

    def __str__(self):
        return self.team_leader

