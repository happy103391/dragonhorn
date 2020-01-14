"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
# Import view functions from trips app.
from marketing.views import index, data,member,rfm
from production.views import material,historyrecord,inventory

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('home/',index),
    path('home/index.html',index),
    path('home/member.html',member),
    path('home/rfm.html',rfm),
    path('home/data.html',data),
    path('home/historyrecord.html',historyrecord),
    path('home/inventory.html',inventory),
    #path('newpage/',views.newpage),
    #url(r'^create/$', 'inventory.views.create'),
    #url(r'^create/$', 'inventory.views.create'),
   # url(r'^cal/$', 'inventory.views.create'),
    path('home/material.html',material),
    url(r'^historyrecord/$', historyrecord),
    
    # url(r'^$', sellsview.as_view(), newpage)
    

]
