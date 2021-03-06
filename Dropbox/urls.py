from django.conf.urls import patterns, include, url
from tastypie.api import Api
from dropbox.api import ContainerResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ContainerResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Dropbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(v1_api.urls)),
)
