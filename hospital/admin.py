from django.contrib import admin

# 导入医生模块
from hospital.models import Doctor

# Register your models here.

admin.site.register(Doctor)