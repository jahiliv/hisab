# Generated by Django 3.2.5 on 2021-07-27 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermoreinfo',
            name='user_type',
        ),
    ]