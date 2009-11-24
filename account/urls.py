from django.conf.urls.defaults import *

urlpatterns = patterns('account.views',

	url(r'^logout/$', 'logout', name='account_logout'),

	# api
	url(r'^api/login/$', 'api_login', name='api_account_login'),
)