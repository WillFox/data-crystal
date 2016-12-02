from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.app_home, name='app_home'),
    url(r'^data/(?P<dataid>\w+)/$', views.data_view, name='simple_data'),
    url(r'^data/', views.data, name='data'),
    url(r'^instrument', views.instrument, name='instrument'),
    url(r'^collection', views.collection, name='collection'),
    url(r'^analysis', views.analysis, name='analysis'),
	]
