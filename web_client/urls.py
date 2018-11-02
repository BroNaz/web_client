#web_client URL Configuration

from django.contrib import admin
from django.conf.urls import url 
from django.views.generic import RedirectView
from django.conf.urls import include
#from django.urls import re_path


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$',RedirectView.as_view(url='/ads/', permanent=True)),  # redirect 
    url(r'^ads/', include('connect.urls')),
]



# Only for the period of development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
