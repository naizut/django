from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.chat_board, name='chat_board'),
]