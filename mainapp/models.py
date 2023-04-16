from dbm.ndbm import library
from email import message
from email.policy import default
from secrets import choice
from django.db import models
import uuid
# Create your models here.



class RegisteredUsers(models.Model):
    # user_id = models.UUIDField(primary_key=True,default=str(uuid.uuid4()))
    user_id = models.UUIDField(default=uuid.uuid4,primary_key=True,max_length=55)
    username = models.CharField(max_length=55)
    name = models.CharField(max_length=55,null=True)
    email = models.CharField(max_length=55, null=True)
    phone = models.CharField(max_length=14, null=True)
    password = models.CharField(max_length=260, null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)
    is_live = models.CharField(max_length=2,default='0')

class RegisteredCollege(models.Model):
    user_id =models.UUIDField(default=uuid.uuid4,primary_key=True,max_length=55)
    name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    phone = models.CharField(max_length=14)
    state = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    area = models.CharField(max_length=55)
    password = models.CharField(max_length=260)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)
    is_live = models.CharField(max_length=2,default='0')

class Contact(models.Model):
    name = models.CharField(max_length=55,null=False)
    email = models.CharField(max_length=55)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)



    