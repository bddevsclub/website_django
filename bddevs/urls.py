from django.conf.urls import patterns, include, url

from django.contrib import admin
from webinar.views import home


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
)

