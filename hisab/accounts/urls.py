from django.urls import path
from accounts import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('index/', views.index, name='index'),
    # path('list/', views.userlist, name='list'),
    # path('amount/', views.amount, name='amount'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.registration, name='registration'),
    
    path('list/', views.userlist, name='list'),
    path('details/', views.details, name='details'),

]