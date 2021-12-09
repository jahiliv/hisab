# from django import forms
# # from django.db import models
# # from django.db.models import fields
# from .models import Users, UsersType
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import Users

# class UserstypeForm(ModelForm):
#     class Meta:
#         models=UsersType
#         fields = ["name"]

# class CreateUsersForm(UserCreationForm):
#     class Meta:
#         models=Users
#         fields= ["firstname", "lastname", "username", "password", "facebookid", "email", "number", "amount", "is_active", "created_at", "updated_at", "deleted_at"]
#         # fields = "_all_"