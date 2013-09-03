from django.conf.urls import patterns, include, url
from polls import urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls', namespace='polls')),
)
