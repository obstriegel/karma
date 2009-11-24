from django.conf.urls.defaults import *

urlpatterns = patterns('item.views',

	url(r'^(?P<id>\d+)/$', 'view', name='item_view'),
	url(r'^add/$', 'add', name='item_add'),

	# api
	url(r'^api/add/$', 'api_add', name='api_item_add'),

 )
