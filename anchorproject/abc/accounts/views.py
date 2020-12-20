from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django import forms
# from .forms import LoginForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from staff.models import Staff_profile
# from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
      
        # staff_id = request.POST['staff_id']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # staff = Staff_profile(staff_id)
        # staff.save()
        # staff = Staff_profile.objects.filter(staff_id=staff_id)
        # messages.error(request,'eyehhh')
        if password1 == password2:
            #    Check username 
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return redirect('signup')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect('signup')

                    else:
                        # looks good    
                        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name)


                        # Login after signup 
                        # auth.login(request, user)
                        # messages.success(request, 'You are now logged in')
                        # return redirect('index')

                        user.save()
                        messages.success(request, 'You are now registered and can log in')
                        return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')    
            return redirect('signup')

    else:

        return render(request, 'accounts/register.html')


def logins(request):
    
    if request.method == 'POST':
       
        username = request.POST['username']
        # staff_id = request.POST['staff_id']
        password = request.POST['password1']
        
        # staff = Staff_profile(staff_id)
        
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('staff')


        else:
            messages.error(request,'Invalid staff ID and password')
            return redirect('login')

    else:
     
        return render(request, 'accounts/login.html')


def logouts(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('login')    




# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         # print(form.errors)    
#         # messages.error(request, messages=form.errors)
#         form = UserCreationForm() 

#     context = {
#         'form':form
#     }
       


   

#     return render(request, 'accounts/register.html', context)

    





# def logins(request):

    
    
#     if request.method == 'POST':
        
#         staff_id = request.POST['staff_id']     

#         user = auth.authenticate(request.POST,staff_id=staff_id)

        

#         if user is not None:
#             messages.error(request,'Invalid credentials')
#             return redirect ('login')
            

#         else:
#             login( request,user, backend='django.contrib.auth.backends.ModelBackend')
#             messages.success(request, 'You are now logged in')
#             return redirect('staff')


#     else:
#         return render (request, 'accounts/login.html')       


# def logins(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST) 
#         if form.is_valid:
#             user = form.get_user()
#             login(request, user)    
#             return redirect('index')
#     else: 
#         form = LoginForm() 
#     return render(request, 'accounts/login.html', {'form':form})


# def logouts(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request,'You are now logged out')
#         return redirect('login')

#     else:
#         return render(request, 'accounts/login.html')    
        