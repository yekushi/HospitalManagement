"""pyweb01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib import staticfiles


from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('add', views.addDoctor),
    url('index', views.findDoctor),
    url('home', views.show,name='home'),
    url('content',views.content),
    url('foot',views.foot),
    url('head',views.head),
    url('nav',views.nav),
    url('service',views.service),
    url('time',views.Time),
    url('healthy',views.Healthy),
    url('depart',views.Depart)
    # url(r'^static/(?P.*)',)
]
# 设置静态文件路径
# urlpatterns += staticfiles_urlpatterns()