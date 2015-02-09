from django.conf.urls import patterns, include, url
from django.contrib import admin

try:
	from views import get_cache_dj_var_js, example_view_var_js
except Exception:
	from var_js.views import get_cache_dj_var_js


urlpatterns = patterns('',
    url(r'^get_cache_dj_var_js/', get_cache_dj_var_js, name='get_cache_dj_var_js'),
    url(r'^admin/', include(admin.site.urls)),
)
