from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import autocomplete_light

autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mobile/', include('mobile.urls',namespace="mobile")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)

urlpatterns += staticfiles_urlpatterns()