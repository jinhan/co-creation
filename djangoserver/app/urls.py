from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.intro, name='intro'),
	url(r'^settings/1', views.selection1, name='selection1'),
	url(r'^settings/2', views.selection2, name='selection2'),
	url(r'^settings/3', views.selection3, name='selection3'),
	url(r'^mode/', views.mode, name='mode'),
	url(r'^settings/d', views.goBack, name='goBack'),
	url(r'^colorize/', views.colorize, name='colorize'),
	url(r'^colorize_post/', views.colorize_post, name='colorize_post'),
	url(r'^colorize_paint/', views.colorize_paint, name='colorize_paint'),
]
