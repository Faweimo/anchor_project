from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Work_log
from staff.models import Staff_profile
def logs(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        department = request.POST['department']
        team_leader = request.POST['team_leader']
        clock_in = request.POST['clock_in']
        work_title = request.POST['work_title']
       
        messages.success(request, 'You are now mark present for today work')
        if request.user.is_authenticated:
            id = request.user.id
            has_submitted = Work_log.objects.all().filter(id=id)
            if has_submitted:
                messages.error(request, 'You have already mark present') 
                return redirect('/staff/' + id)
        log =Work_log.objects.all(first_name=first_name,department=department,team_leader=team_leader,clock_in=clock_in,work_title=work_title)
        log.save()
        return redirect('/staff/' + id)

