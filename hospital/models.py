from django.db import models

# Create your models here.

class Doctor(models.Model):
    # 医生类
    username = models.CharField(primary_key=True, max_length=20)
    usersex = models.CharField(max_length=2)
    institution = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    userage = models.IntegerField(max_length=20)
    type = models.BooleanField(max_length=2)
    address = models.TextField(max_length=200)
    tel = models.CharField(max_length=20)