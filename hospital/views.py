from django.shortcuts import render
from django.shortcuts import redirect

from django.db.models import Q
from hospital.models import Doctor
# Create your views here.

# 添加医生信息
def addDoctor(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_sex = request.POST.get('user_sex')
        Doctor.objects.create(username=user_name, usersex=user_sex)
        return redirect('index.html')

# 查找ALL
def showAll(request):
    doctors = Doctor.objects.all()
    count = doctors.__len__()
    return render(request, 'index.html', context={'count':count})

# 出诊时间
def Time(request):
    return  render(request,'time.html')
# 健康知识
def Healthy(request):
    return render(request,'healthy.html')
# 科室导航
def Depart(request):
    return render(request,'depart.html')

# 显示home
def show(request):
    return render(request,'home.html')
# 模糊查找信息
def findDoctor(request):
    sousuo = request.POST.get('sousuo')
    doctors = Doctor.objects.filter(Q(username__icontains=sousuo)|Q(usersex__icontains=sousuo))
    return render(request,'index.html', context={'doctors':doctors,'count':doctors.__len__()})
# header/nav/content/footer
def head(request):
    return render(request,'header.html')
def content(request):
    return render(request,'content.html')
def foot(request):
    return render(request,'footer.html')
def nav(request):
    return render(request,'nav.html')

# 病友服务
def service(request):
    return render(request,'service.html')