from django.db import models
from django.contrib.auth.models import User
import datetime
# from django.utils import timezone

# import pytz
# from django.utils.timezone.now import timezone
# Create your models here.

class Attendance(models.Model):
    attendance_id = models.IntegerField(primary_key=True,default=1)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    team_leader = models.CharField(max_length=200)
    clock_in = models.DateTimeField(default=datetime.datetime.now(),blank=False,null=False)
    work_title = models.CharField(max_length=200,blank=False,null=False)
    email = models.EmailField(default=' ')

    def __str__(self):
        return self.name
