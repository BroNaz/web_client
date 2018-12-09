## @package WEB_USERS
#  Module control for application "users"

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import registration
from django.http import HttpResponse
from django.shortcuts import redirect
import requests

# base url database
url_root = 'https://protected-bayou-62297.herokuapp.com'

## User delete function.
#
#  is available to the user only with the correct data cookie value
def delete(request):
    if 'session_id' in request.COOKIES:
        if request.method =="POST":
            url = url_root + '/users/profile'
            headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            'Cookie': request.COOKIES['session_id'],
            }
            resp = requests.delete(url, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                response = redirect("/")
                response.delete_cookie("session_id")
                return response
            else: 
                return HttpResponse(resp.status_code)
        else:
            return render(request, "users/delete.html")
    else:
        return redirect("/users/login/")


## User login function.
#
#  sends a password and email to the database for comparison, receives a cookie in return "session_id"
#  render "users/logout.html" if the user is already with cookies
#  render "users/login.html" if the user is without cookies
def login(request):
    if 'session_id' in request.COOKIES: 
        return render(request, "users/logout.html")
    else:
        if request.method == "POST":
            url = url_root + '/users/login'
            userdata = {
                'email': request.POST.get("email"),
                'password': request.POST.get("password"),
            }
            headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            }
            resp = requests.post(url, data=userdata, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                response = redirect('/')
                parser = resp.headers['Set-Cookie']
                expires = parser[65:94]
                response.set_cookie('session_id', resp.headers['Set-Cookie'], expires=expires)
                return  response 
            else :
                return HttpResponse("err")  
        else:
            return render(request, "users/login.html")


## User logout function.
#
#  is available to the user only with the correct data cookie value
def logout(request):
    if 'session_id' in request.COOKIES:
        response = redirect("/")
        response.delete_cookie("session_id")
        return response
    else:
        return HttpResponse("err")

## Сreate new user function
#
#  sends a password and email to the database fields email, password, first_name, last_name, tel_num, about from the template "users/new_users.html"
def new_users(request):
    if request.method == "POST":
        url = url_root + '/users/new' 
        userdata = {
            'email': request.POST.get("email"),
            'password': request.POST.get("password"),
            'first_name': request.POST.get("first_name"),
            'last_name': request.POST.get("last_name"),
            'tel_number': request.POST.get("tel_num"),
            'about': request.POST.get("about"),
            }
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            }
        resp = requests.post(url, data=userdata, headers=headers)
        if (resp.status_code >= 200) and (resp.status_code<=300) :
            response = redirect('/')
            return  response 
        else :
            return HttpResponse("err")   
    else:
        return render(request, "users/new_users.html", )


## User information function.
#
#  is available to the user only with the correct data cookie value
#  function that provides information about the registered account (own account)
#  takes json 
#  json example : 
#   {
#   "id": 123456,
#   "first_name": "Random",
#   "last_name": "Valerka",
#   "email": "valerka@example.com",
#   "tel_number": "1-234-56-78",
#   "about": "Some information about this man",
#   "time_reg": "2012.10.1 15:34:41"
#   }
def info(request):
    if 'session_id' in request.COOKIES:
        url = url_root + '/users/profile'
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            'Cookie': request.COOKIES['session_id'],
            }
        resp = requests.get(url, headers=headers)
        if (resp.status_code >= 200) and (resp.status_code<=300) :
            return render(request, "users/info.html", resp.json())
        else:
            return HttpResponse(resp.status_code) # отрисовать стр ошибок  
    else:
        return redirect('/users/login/')


## User update function.
#
#  is available to the user only with the correct data cookie value
#  sends a password and email to the database fields email, password, first_name, last_name, tel_num, about from the template "users/update.html"
#  at get request it requests the same json as in "def info(request)"
def update(request):
    if 'session_id' in request.COOKIES:
        if request.method == "POST":
            userdata = {
                'email': request.POST.get("email"),
                'password': request.POST.get("password"),
                'first_name': request.POST.get("first_name"),
                'last_name': request.POST.get("last_name"),
                'tel_number': request.POST.get("tel_num"),
                'about': request.POST.get("about"),
            }
            url = url_root + '/users/profile'
            headers = {
                'user-agent': request.META['HTTP_USER_AGENT'],
                'Cookie': request.COOKIES['session_id'],
            }
            resp = requests.post(url, headers=headers, data=userdata)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                resp = requests.get(url, headers=headers)
                return render(request, "users/info.html", resp.json())
            else:
                return HttpResponse(resp.status_code) # отрисовать стр ошибок
        else:
            url = url_root + '/users/profile'
            headers = {
                'user-agent': request.META['HTTP_USER_AGENT'],
                'Cookie': request.COOKIES['session_id'],
            }
            resp = requests.get(url, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                return render(request, "users/update.html", resp.json())
            else:
                return HttpResponse(resp.status_code) # отрисовать стр ошибок
    else :
        return redirect('/users/login/')
