from django.contrib.auth.models import User
from django.db import models
from datetime import datetime    

class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=90)
    address = models.CharField(max_length=255)
    start_working_hour = models.TimeField(null=True,blank=True)
    end_working_hour = models.TimeField(null=True,blank=True)

class Division(models.Model):
    company = models.ForeignKey(Company,related_name='FK_Division_Company',on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)

class Position(models.Model):
    company = models.ForeignKey(Company,related_name='FK_Position_Company',on_delete=models.PROTECT)
    division = models.ForeignKey(Division,related_name='FK_Position_Division',on_delete=models.PROTECT,null=True,blank=True)
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)

class EmployeeType(models.Model):
    company = models.ForeignKey(Company,related_name='FK_EmployeeType_Company',on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

class EmployeePayType(models.Model):
    name = models.CharField(max_length=50)

class Employee(models.Model):
    user = models.OneToOneField(User,related_name='FK_Employee_user',on_delete=models.PROTECT,unique=True)
    company = models.ForeignKey(Company,related_name='FK_Employee_Company',on_delete=models.PROTECT,null=True,blank=True)
    position = models.ForeignKey(Position,related_name='FK_Employee_position',on_delete=models.PROTECT,null=True,blank=True)
    type = models.ForeignKey(EmployeeType,related_name='FK_Employee_EmployeeType',on_delete=models.PROTECT,null=True,blank=True)
    pay_type = models.ForeignKey(EmployeePayType,related_name='FK_Employee_EmployeePayType',on_delete=models.PROTECT,null=True,blank=True)
    pay_rate = models.IntegerField(default=0)

class Attandance(models.Model):
    user = models.OneToOneField(User,related_name='FK_Attandance_user',on_delete=models.PROTECT,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)

class Message(models.Model):
    from_user = models.OneToOneField(User,related_name='FK_Message_from_user',on_delete=models.PROTECT,unique=True)
    to_user = models.OneToOneField(User,related_name='FK_Message_to_user',on_delete=models.PROTECT,unique=True)
    message= models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

class Feed(models.Model):
    company = models.ForeignKey(Company,related_name='FK_Feed_Company',on_delete=models.PROTECT,null=True,blank=True)
    message = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

class AttendaceCode(models.Model):
    company = models.ForeignKey(Company,related_name='FK_AttendaceCode_Company',on_delete=models.PROTECT,null=True,blank=True)
    secret_key = models.TextField(blank=False, null=False)
