from django.db import models
# from django.db.models.fields import EmailField

# Create your models here.

class UsersType(models.Model):

    name = models.CharField(max_length=100)

class Meta:
    Model = "userstype"

class Users(models.Model):

    user_type = models.ForeignKey(UsersType,on_delete=models.CASCADE,default=None)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField()
    amount = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

class Meta:
    Model = "users"

    # def __str__(self):
    #     return str(self.pk)+ " " + self.firstname + " " + self.lastname
    
