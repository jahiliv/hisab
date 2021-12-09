from django.urls import path
from collection import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    # path('list/', views.userlist, name='list'),
    path('amount/', views.amount, name='amount'),
    path('myprofile/', views.myprofile, name='myprofile'),
    # path('signin/', views.login, name='login'),
    # path('signup/', views.registration, name='registration'),

]