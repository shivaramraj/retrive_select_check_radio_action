"""project18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Insert_topic/',Insert_topic,name='Insert_topic'),
    path('Insert_webpage/',Insert_webpage,name='Insert_webpage'),
    path('display_webpages/',display_webpages,name='display_webpages'),
    path('retrive_webpages/',retrive_webpages,name='retrive_webpages'),
    path('retrive_web_checkbox/',retrive_web_checkbox,name='retrive_web_checkbox'),
    path('retrive_web_radio/',retrive_web_radio,name='retrive_web_radio'),
]
