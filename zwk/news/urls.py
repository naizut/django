from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.news_list, name='news_list'),
	url(r'^(?P<news_id>\d+)/$', views.news_content, name='news_content'),
	url(r'^like-news/$', views.newsLikes, name='like_news'),
]