from django.conf.urls.defaults import *
from django.conf import settings
import os

urlpatterns = patterns('dreque_frontend.views',
    url(r'^$', 
        view='overview',
        name='dreque_overview'),
    
    url(r'^queue/(?P<queue_name>[-\w]+)/$',
        view='queue_detail',
        name='dreque_queue_detail'),
)
