from django.shortcuts import render,redirect 
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from .models import Log


def loger(request):
   if request.method == 'POST':
       work_id = request.POST['work_id']
       full_name = request.POST['full_name']
       email = request.POST['email']
       department = request.POST['department']
       team_leader = request.POST['team_leader']
       work_title = request.POST['work_title']
       clock_in = request.POST['clock_in']
       user_id = request.POST['user_id']


       if request.user.is_authenticated:
           user = request.user.id
           has_logged = Log.objects.all().filter(work_id=work_id,user_id=user_id)
           if has_logged:
               messages.error(request, 'You are already logged')
           return redirect('/login/' +work_id )

       log=Log(work_id=work_id,full_name=full_name,email=email,department=department,team_leader=team_leader,work_title=work_title,clock_in=clock_in,user_id=user_id)

       log.save()

       return redirect('/login/' +work_id )


