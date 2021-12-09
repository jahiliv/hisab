from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.models import Users
from collection.models import UsersType, Users
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"base.html")
    return HttpResponse('<h1>Blog</h1>')


# def home(request):
#     return render(request,"home.html")
@login_required
def myprofile(request):
    return render (request, "myprofile.html")

# def userlist(request):
#     user = User.objects.all()
#     return render(request,"list.html", {'user':user})

@login_required
def amount(request):
    return render(request,"amount.html")

# def login(request):
#     return render(request,"login.html")

# def registration(request):
#     return render(request,"registration.html")



# def registration(request):
#     if request.method == 'POST':
#         if request.POST.get('firstname') and request.POST.get('lastname')and request.POST.get('username')and request.POST.get('facebookid')and request.POST.get('password')and request.POST.get('email')and request.POST.get('number'):
#             saverecord = Users
#             saverecord.firstname=request.POST.get('firstname')
            
#             saverecord.lastname=request.POST.get['lastname']
#             saverecord.username=request.POST.get['username']
#             saverecord.facebookid=request.POST.get['facebookid']
#             saverecord.password = request.POST.get['password']
#             saverecord.email=request.POST.get['email']
#             saverecord.number=request.POST.get['number']
#             saverecord.is_active = 0
#             saverecord.amount = 0
#             saverecord.usertype = 3
#             saverecord.save()
#             messages.success(request, 'Congratulations')
#             return render(request,'home.html')
#     else:
#             return render(request,'registration.html')

        # firstname=request.POST['firstname']
        # lastname=request.POST['lastname']
        # username=request.POST['username']
        # facebookid=request.POST['facebookid']
        # password = request.POST['password']
        # email=request.POST['email']
        # number=request.POST['number']
        # is_active = 0
        # amount = 0
        # usertype = 3
        # users = Users.objects.create_user(firstname=firstname, lastname=lastname, username=username, 
        # password=password, facebookid=facebookid, email=email,
        # number=number, is_active=is_active, amount=amount).save()
        # messages.success(request, 'Congratulations')
    #     return render(request,"registration.html")
    # else:
    #     return render(request,"registration.html")
        