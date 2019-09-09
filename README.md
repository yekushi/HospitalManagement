# 关于
这是由django框架搭建的一个简单的基于python-web的医院网站，可实现管理员的增删改查以及给予医生的权限，医生和病人的查询流程。
* hospital：应用APP
* pyweb01：项目的容器
* manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
* static：static称为静态文件夹，用于存放CSS, JavaScript, 网站logo等不变的文件。（相对的，把media称为媒体文件夹，用于存放用户上传的图片。）
* templates：web页面
* Requirements.txt：项目所依赖的包
# 使用指南

前提：需要自行设置mysql用户名及密码

1、在终端安装项目依赖包
* pip install -r Requirements.txt

2、做数据迁移备份和数据迁移
* python manage.py makemigrations
* python manage.py migrate

3、启动django开发服务器
* python manage.py runserver

4、在浏览器访问127.0.0.1：8000，并访问首页home.html(127.0.0.1:8000/home.html)即可运行简单的django项目，可继续添加功能。

注意：项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启。

使用mysql数据库

如果出现：

mysqlclient 1.3.13 or newer is required; you have 0.9.3.

将__init__.py文件中的代码注释掉：

import pymysql

pymysql.install_as_MySQLdb()

直接安装mysqlclient--pip install mysqlclient
