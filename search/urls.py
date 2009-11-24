from django.conf.urls.defaults import *

urlpatterns = patterns('search.views',

	# api
	url(r'^api/search/$', 'api_search', name='api_search_search'),

)
