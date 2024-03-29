#from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjangoApp.views.home', name='home'),
    # url(r'^MyDjangoApp/', include('MyDjangoApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),
#)
from django.conf.urls.defaults import patterns, include

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    (r'^polls/$', 'MyDjangoApp.polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'MyDjangoApp.polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'MyDjangoApp.polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'MyDjangoApp.polls.views.vote'),
    (r'^admin/', include(admin.site.urls)),
)