from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
	url(r'^$', 'index', name='index'),
	url(r'^(?P<poll_id>\d+)/$', 'detail', name='detail'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),
	# url(r'^(?P<poll_id>\d+)/vote/(?P<choice_id>\d+)/$', 'vote', name='vote'),
	url(r'^(?P<poll_id>\d+)/result/$', 'result', name='result'),
)
