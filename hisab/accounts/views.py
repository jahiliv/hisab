# from collection.views import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import usermoreinfo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    # log_user = request.user
    return render(request,"home.html")


def login(request):
    if request.method == "POST":
        logername = request.POST['username']
        logerpassword = request.POST['password']
        user=auth.authenticate(username=logername, password=logerpassword)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            return render(request,"login.html", {'error': "Invalid Login Credentials."})
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect(login)

def registration(request):
    if request.method == "POST":

        # if request.POST['password'] == request.POST['repassword']:
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'registration.html', {'error': "Username has already taken."})
        except User.DoesNotExist:
            user = User.objects.create_user(first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],email=request.POST['email'],
            username=request.POST['username'], password = request.POST['password'])
            phonenumber = request.POST['phone']
            facebookid = request.POST['facebookid']
            userextendedinfo = usermoreinfo(number=phonenumber,facebookid=facebookid,user=user)
            userextendedinfo.save()
            # 3 = request.POST['user_type']
            # phonenumber = request.POST['phone']
            
            return redirect(login)

        # else:
        #     return render(request, 'registration.html', {'error': "Password doesn't match. Please Try Again"})
    else:
        return render(request,"registration.html")

@login_required
def userlist(request):
    # log_user= request.User
    # user = User.objects.all()
    # user= usermoreinfo.objects.filter(log_user)
    user = usermoreinfo.objects.all()
    # print(user)
    return render(request,"list.html", {'user':user})

@login_required
def details(request):
    return render(request,"details.html")