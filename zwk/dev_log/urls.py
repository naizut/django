from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.devlogList, name='coding-titles'),
	url(r'^(?P<coding_id>\d+)/$', views.devlogContent, name='coding-content'),
	# url(r'^likes-coding/$', views.codingLikes, name='coding-likes')
	url(r'^search-titles/$', views.searchTitles, name='titles-search'),
	url(r'^search-titles/(?P<coding_id>\d+)/$', views.devlogContent, name='coding-content'),
	# url(r'^filter_by_labels/$', views.devlogListByLabels, name='filter_by_labels'),
	# url(r'^filter_by_category/$', views.devlogListByCategory, name='filter_by_category'),
	# url(r'^filter_by_language/$', views.devlogListByLanguage, name='filter_by_language'),
	url(r'^filter_by_sort/(?P<coding_sort>\w+)/$', views.devlogList, name='filter_by_sort'),
	url(r'^filter_by_sort/\w+/(?P<coding_id>\d+)/$', views.devlogContent, name='content_sort'),
	url(r'^filter_by_language/(?P<coding_language>\w+)/$', views.devlogList, name='filter_by_language'),
	url(r'^filter_by_language/\w+/(?P<coding_id>\d+)/$', views.devlogContent, name='content_language'),
	url(r'^filter_by_category/(?P<coding_category>\w+)/$', views.devlogList, name='filter_by_category'),
	url(r'^filter_by_category/\w+/(?P<coding_id>\d+)/$', views.devlogContent, name='content_category'),
	url(r'^filter_by_labels/(?P<coding_labels>\w+)/$', views.devlogList, name='filter_by_labels'),
	url(r'^filter_by_labels/\w+/(?P<coding_id>\d+)/$', views.devlogContent, name='content_labels'),

]