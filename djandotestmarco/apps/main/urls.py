__author__ = 'marco'
from django.conf.urls import patterns, url

urlpatterns = patterns('djandotestmarco.apps.main.views',
                       url(r'^$','index_view',name='url_index'))