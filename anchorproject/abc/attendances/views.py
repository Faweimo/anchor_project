from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Attendance
from staff.models import StaffProfile
from django.core.mail import send_mail
from staff.models import StaffProfile


def attendances(request):
    if request.method == 'POST':
        name = request.POST['name']
     
        team_leader = request.POST['team_leader']
        # attendance_id = request.POST['attendance_id']
        work_title = request.POST['work_title']
        clock_in = request.POST['clock_in']
        email = request.POST['email']

        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_messaged = Attendance.objects.all().filter(clock_in=clock_in,name=name)
        #     if has_messaged:
        #         messages.error(request,'You are already marked present')
        #         return redirect('staff')

        attendance = Attendance(name=name,team_leader=team_leader,work_title=work_title,email=email)

        attendance.save()

        #send email

        # send_mail(
        #     'Staff Attendance',
        #     'You are already mark present today' + name + 'Remember to logout after the close the work' ,
        #     'syllabus28@gmail.com',
        #     [email,'f.owolabi81@gmail.com'],
        #     fail_silently=False

        # )

        messages.success(request,'You are present for today work')
        return redirect('staff')


        