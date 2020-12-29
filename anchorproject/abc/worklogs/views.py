from django.shortcuts import render,redirect 
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from .models import Logger
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import LoggerForm


def logger(request):
   if request.method == 'POST':
       full_name = request.POST['full_name']
       email = request.POST['email']
       department = request.POST['department']
       team_leader = request.POST['team_leader']
       work_title = request.POST['work_title']
    #    clock_in = request.POST['clock_in']
       work_id = request.POST['work_id']
       user_id = request.POST['user_id']


       if request.user.is_authenticated:
           user = request.user.id
           has_logged = Logger.objects.all().filter(user_id=user_id)
           if has_logged:
               messages.error(request, 'You are already logged')
               return redirect('staff')

       log=Logger(full_name=full_name,email=email,department=department,team_leader=team_leader,work_title=work_title,user_id=user_id,work_id=work_id)

       log.save()



       # send email
       send_mail(
           'Staff Daily Attendance',
           'You are now mark present for today work ' + full_name + 'Sign into the panel for more info',
           'syllabus28@gmail.com',
           [email,'f.owolabi81@gmail.com'],
           fail_silently= False,
       )


       messages.success(request, 'You are now mark present')


       return redirect('staff')


# def logger(request):
#     if request.method == 'POST':
#         form = LoggerForm(request.POST)
#         if form.is_valid():
#            form.save()
#            messages.success(request, 'You are now mark present') 



        #    send_mail(
        #     'Staff Daily Attendance',
        #     'You are now mark for today work ' + form.full_name + ', Sign into the admin panel for more info',
        #     'syllabus28@gmail.com',
        #     [form.email, 'f.owolabi81@gmail.com'],
        #     fail_silently = False,
        # )

        #    return redirect('staff')


        # else:
        #     form = LoggerForm()

        # context = {
        #     'form':form
        # }    
        # return render(request,'staff/index.html',context)




