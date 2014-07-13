from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mobile import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<soul_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^submit', views.submit, name='submit'),
    url(r'^postJson$', views.postJson, name='postJson'),
]