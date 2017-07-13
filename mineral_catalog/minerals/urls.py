from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'^(?P<pk>\d+)$', views.mineral_detail, name='detail'),
    url(r'^random$', views.random, name='random'),
    url(r'^filter/(?P<letter>[A-Z])$', views.filter_by, name='filter'),
    url(r'^search', views.search, name='search'),
    url(r'^filter_by_category/(?P<category>[ \w]+)$', views.filter_by_category,
        name='filter_by_cate'),
]
