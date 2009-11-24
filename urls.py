from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/filebrowser/', include('filebrowser.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^admin/(.*)', admin.site.root),

	url(r'^$', 'views.index', name='index'),

	url(r'^account/', include('account.urls')),
	url(r'^item/', include('item.urls')),
	url(r'^search/', include('search.urls')),

)

from django.conf import settings
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
			'show_indexes': True
		})
	)
