# Generated by Django 3.2.5 on 2021-07-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_usermoreinfo_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoreinfo',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]