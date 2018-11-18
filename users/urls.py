from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('<int:question_id>/delete/', views.delete, name='delete'),
    path('new/', views.new_users, name='new_users'),
    path('<int:question_id>/', views.info, name='info'),
    path('<int:question_id>/update/', views.update, name='update'),
]