from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.load_list, name='load_list'),
    url(r'^load/(?P<pk>\d+)/$', views.load_detail, name='load_detail'),
    url(r'^load/new/$', views.load_new, name='load_new'),
    url(r'^load/(?P<pk>\d+)/edit/$', views.load_edit, name='load_edit'),
]