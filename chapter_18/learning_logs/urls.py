""" define learning_logs url pattern """

from django.conf.urls import url, include	

from . import views

urlpatterns = [
	# homepage
	url(r'^$', views.index, name='index'),

	# display all topics
	url(r'^topics/$', views.topics, name='topics'),

	# display special topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]