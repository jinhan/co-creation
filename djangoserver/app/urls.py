from django.conf.urls import url
from . import views
# from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.intro, name='intro'),
	url(r'^settings/1', views.selection1, name='selection1'),
	url(r'^settings/2', views.selection2, name='selection2'),
	url(r'^settings/3', views.selection3, name='selection3'),
	url(r'^draw/', views.draw, name='draw'),
	url(r'^settings/d', views.goBack, name='goBack'),
]
