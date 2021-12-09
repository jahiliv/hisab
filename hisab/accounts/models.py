from collection.models import UsersType
from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class usermoreinfo(models.Model):
    # user_type = models.ForeignKey(UsersType,on_delete=models.CASCADE,default=None)
    facebookid = models.CharField(max_length=200)
    # email = models.EmailField()
    number = models.IntegerField()
    amount = models.IntegerField(null=True)
    is_active = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)