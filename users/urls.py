from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('delete/', views.delete, name='delete'),
    path('new/', views.new_users, name='new_users'),
    path('info/', views.info, name='info'),
    path('update/', views.update, name='update'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]