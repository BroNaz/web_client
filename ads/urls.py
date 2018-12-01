from django.urls import path

from . import views

app_name = 'ads'
urlpatterns = [
   #path('<int:page>/', views.home_page, name='home_page'),
   path('new/', views.new, name='new'),
   path('<int:id>/', views.ad, name='ad'),
   path('<int:id>/update/', views.update, name='update'),
   path('<int:id>/delete/', views.delete, name='delete'),
   path('all/<int:id>/',views.all_ads , name='all_ads'),
   path('myads/', views.myads, name='myads'),
]