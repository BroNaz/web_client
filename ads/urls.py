from django.urls import path

from . import views

app_name = 'ads'
urlpatterns = [
   path('<int:page>/', views.home_page, name='home_page'),
   path('new/', views.new, name='new'),
   path('<int:id>/<int:id_ad>/', views.ad, name='ad'),
   path('<int:question_id>/update/', views.update, name='update'),
   path('<int:question_id>/delete/', views.delete, name='delete'),
]