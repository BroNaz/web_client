## @package WEBROOT
#  Main module control and url redirection
#
#  for the path "/ads" redirect to the application "ads"
#  for the path "/users" redirect to the application "users"
#  for the path "", "<int:page>/", "<str:search>/", "<str:search>/<int:page>/" function is connected from the application "ads"

from django.contrib import admin
from django.urls import include, path
from ads.views import home_page, search, asd

urlpatterns = [
    path('ads/', include('ads.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('',home_page),
    path('<int:page>/',home_page, name ='home'),
    path('<str:search>/',home_page, name='search'),
    path('<str:search>/<int:page>/',home_page, name='search_page'),
]
