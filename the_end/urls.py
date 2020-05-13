"""the_end URL Configuration

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
from django.conf.urls import *
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url('time/$', time, {'text': 'time.html'}),
    url(r'^time/plus/\d{1,2}/$', hours_head, {'offset': 5}),
    url(r'meta/$', display_meta),
    url(r'search/$', search),
    url(r'^在？我不想学机械/$', time, {'text': 'timechange.html'}),
    url(r'contact/$', contact),
]
