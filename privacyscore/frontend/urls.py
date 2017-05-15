from django.conf.urls import url

from privacyscore.frontend import views

app_name = 'frontend'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^info/$', views.info, name='info'),
    url(r'^legal/$', views.legal, name='legal'),
    url(r'^list/$', views.list_view, name='list'),
    url(r'^login/$', views.login, name='login'),
    url(r'^lookup/$', views.lookup, name='lookup'),
    url(r'^scan/$', views.scan, name='scan'),
    url(r'^scanned_list/$', views.scanned_list, name='scanned_list'),
    url(r'^third_parties/$', views.third_parties, name='third_parties'),
    url(r'^user/$', views.user, name='user'),
]