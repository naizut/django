from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.games_pics, name='games_pics'),
	url(r'^csgo/', views.games_csgo, name='games_csgo'),
	# url(r'^eve/', views.games_eve, name='games_eve'),
	url(r'^fifa14/', views.games_fifa14, name='games_fifa14'),
]