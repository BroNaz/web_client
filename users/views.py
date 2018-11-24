from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import registration
from django.http import HttpResponse
from django.shortcuts import redirect
import requests

url_par = 'http://127.0.0.1:8080'


def delete(request):
    return render(request, "users/delete.html")

def login(request):
    if 'session_id' in request.COOKIES:
        # req отправить на проверку cooki ?? 
        return render(request, "users/logout.html")
    else:
        if request.method == "POST":
            url = 'http://127.0.0.1:8080/users/login'
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
                #session_id = parser[11:55]
                expires = parser[65:94]
                #return HttpResponse(parser[65:94]) #Content-TypeSet-CookieDateContent-Length
                response.set_cookie('session_id', resp.headers['Set-Cookie'], expires=expires)
                return  response 
            else :
                return HttpResponse("err") # отрисовать стр ошибок  
        else:
            return render(request, "users/login.html")

def logout(request):
    if 'session_id' in request.COOKIES:
        response = redirect("/")
        response.delete_cookie("session_id")
        return response
    else:
        return HttpResponse("err")


def new_users(request):
    if request.method == "POST":
        url = 'http://127.0.0.1:8080/users/new' # url - для POST отправки
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
            #response.set_cookie('session_id', resp.headers['session_id']) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return  response # отрисовать стр успешной рег render(request, "users/registration_ok.html")
        else :
            return HttpResponse("err") # отрисовать стр ошибок  
    else:
        return render(request, "users/new_users.html", )

def info(request):
    """
    # принимает JSON и выводит информацию 
    # пример JSON 
    # ниже пример ( отладочный ) JSON  
    info = {
    "id": 123456,
    "first_name": "Random",
    "last_name": "Valerka",
    "email": "valerka@example.com",
    "tel_number": "1-234-56-78",
    "about": "Some information about this man",
    "time_reg": "2012.10.1 15:34:41"
    }
    """
    if 'session_id' in request.COOKIES:
        url = 'http://127.0.0.1:8080/users/profile'
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
            url = 'http://127.0.0.1:8080/users/profile'
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
            # принимает JSON и выводит информацию  
            # ниже пример JSON  
            #info = {
            #"id": 123456,
            #"first_name": "Random",
            #"last_name": "Valerka",
            #"email": "valerka@example.com",
            #"tel_number": "1-234-56-78",
            #"about": "Some information about this man",
            #"time_reg": "2012.10.1 15:34:41"
            #}
            url = 'http://127.0.0.1:8080/users/profile'
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
