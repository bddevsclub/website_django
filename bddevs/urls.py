from django.conf.urls import patterns, include, url

from django.contrib import admin
from webinar.views import home, webinar_view


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
    url(r'^webinar/(?P<id>\d+)', webinar_view, name='webinar_view')
)

