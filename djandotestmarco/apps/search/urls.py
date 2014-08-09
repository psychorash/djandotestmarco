from django.conf.urls import patterns, url
from djandotestmarco.apps.search import views

urlpatterns = patterns('djandotestmarco.apps.search.views',
                       url(r'^search/$', views.SearchView.as_view(), name='search'),

                       )
