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

	# add new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# add new entry page
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# edit entry page
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]