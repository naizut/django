from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^register/$', views.register, name='user_register'),
	url(r'^login/$', views.login, {'template_name':'account/login.html'}, name='user_login'),
	url(r'^logout/$', auth_views.logout, {'template_name':'account/logout.html'}, name='user_logout'),
]