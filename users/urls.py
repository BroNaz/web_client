# -*- coding: utf-8 -*-

"""
 WEB_USERS
  Module control and url redirection for application "users"

  for the path "delete/" redirect to the function delete defined in the file views
  for the path "new/" redirect to the function new_users defined in the file views
  for the path "info/" redirect to the function info defined in the file views
  for the path "update/" redirect to the function update defined in the file views
  for the path "login/" redirect to the function login defined in the file views
  for the path "logout/" redirect to the function logout defined in the file views
"""

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