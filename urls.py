from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as views

urlpatterns = [

	url(r'^$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^register/success/$', views.register_success, name='register_success'),
    	url(r'^accounts/login/$', views.login),
    	url(r'^logout/$', views.logout_page),
]
