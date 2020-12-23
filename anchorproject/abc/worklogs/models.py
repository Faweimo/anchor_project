from django.db import models
import datetime
# Create your models here.
class Log(models.Model):
    work_id = models.IntegerField()
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    department = models.CharField(max_length=200,blank=True,null=True)
    team_leader = models.CharField(max_length=200)
    work_title = models.CharField(max_length=200)
    clock_in = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)


    def __str__(self):
        return self.full_name

