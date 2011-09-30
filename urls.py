from django.conf.urls.defaults import patterns, include, url
from gmap.views import index, showmap, markers, gmap_search, categories, dump_csv, director_by_boundary

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^markers.json$', markers, name="markers"),
    url(r'^categories.json$', categories, name="categories"),
    url(r'^directors/(?P<boundary_code>.+)/$', director_by_boundary, name="directors"),
    url(r'^search/?', gmap_search, name="gmap_search"),
    url(r'^(?P<address>\w+)$', showmap, name="show_map"),
    url(r'^csv/?', dump_csv, name="dump_csv"),
)
