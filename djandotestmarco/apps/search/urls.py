from django.conf.urls import patterns, url
from djandotestmarco.apps.search import views

urlpatterns = patterns('djandotestmarco.apps.search.views',
                       url(r'^$', views.SearchView.as_view(), name='search'),
                       url(r'^json/$', views.UserProfileAJAXView.as_view(), name='json'),

                       )
