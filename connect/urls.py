
#from django.conf.urls import path
from django.conf.urls import url
#from django.urls import re_path
from connect.views import after_ads, ads

urlpatterns = [
    url(r'^$',ads ),
    url(r'^(?P<val>[0-9]+)/$',after_ads), 
    url(r'^(?P<val>[-\w]+)/$',after_ads),
]
