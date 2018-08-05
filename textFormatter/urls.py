# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 21:34:12 2018

@author: kmy07
"""

from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
    path(r'^handshake/$',views.handshake),
    path('bold/',views.makeItBold),
    url(r'^$',views.homepage),
]