from django.conf.urls.defaults import *
from django.conf import settings
from manager import VarnishManager


urlpatterns = patterns('varnishapp.views',
    url(r'', 'management', name="django_varnish_management"),
)
