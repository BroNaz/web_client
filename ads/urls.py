## @package WEB_ADS
#  Module control and url redirection for application "ads"
#
#  for the path "<int:id>/delete/" redirect to the function delete defined in the file views
#  for the path "new/" redirect to the function new defined in the file views
#  for the path "<int:id>/" redirect to the function ad defined in the file views
#  for the path "<int:id>/update/" redirect to the function update defined in the file views
#  for the path "all/<int:id>" redirect to the function all_ads defined in the file views
#  for the path "myads/" redirect to the function myads defined in the file views

from django.urls import path

from . import views

app_name = 'ads'
urlpatterns = [
   path('new/', views.new, name='new'),
   path('<int:id>/', views.ad, name='ad'),
   path('<int:id>/update/', views.update, name='update'),
   path('<int:id>/delete/', views.delete, name='delete'),
   path('all/<int:id>',views.all_ads , name='all_ads'),
   path('myads/', views.myads, name='myads'),
]