"""tp_dz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from noter.views import *

urlpatterns = [
    path('login/<int:log>/', login),
    path('reg/<int:log>/', regist),
    path('logout/', log_out, name="logout"),
    path('del_note/', del_note),
    re_path(r'^l', login, name='login'),
    path('reg/', regist, name='regist'),
    path('read_only/', locker),
    re_path(r'^r', regist),

    path('admin/', admin.site.urls),
    path('get_note/', get_note, name='get_one'),
    re_path(r'', index)
]
