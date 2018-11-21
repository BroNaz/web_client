from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import registration
from django.http import HttpResponse

url_par = 'http://127.0.0.1:80000'

# На данном этапе реализации отладка ведется через 
# внутренние поля (смотреть файл models.py в соответствующей директории),
# в дальнейшей реализации ожидается связь с серверной частью 

def delete(request, question_id):
    return render(request, "users/delete.html")


def new_users(request):
    if request.method == "POST":
        url = url_par + '/users/new' # url - для POST отправки
        userdata = {
            'email': request.POST.get("email"),
            'password': request.POST.get("password"),
            'first_name': request.POST.get("first_name"),
            'last_name': request.POST.get("last_name"),
            'tel_num': request.POST.get("tel_num"),
            'about': request.POST.get("about"),
            }
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            }
        resp = requests.post(url, data=userdata, headers=headers)
        if (resp.status_code >= 200) and (resp.status_code<=300) :
            response = HttpResponse('cookie')
            response.set_cookie('session_id', resp.headers['session_id'])
            return render(request, "users/registration_ok.html") # отрисовать стр успешной рег
        else :
            return HttpResponse("err") # отрисовать стр ошибок  
    else:
        return render(request, "users/new_users.html", )

def info(request, question_id):
    """
    # принимает JSON и выводит информацию 
    # пример JSON 
    # ниже пример ( отладочный ) JSON  
    info = {
    "id": 123456,
    "first_name": "Random",
    "last_name": "Valerka",
    "email": "valerka@example.com",
    "tel_num": "1-234-56-78",
    "about": "Some information about this man",
    "time_reg": "2012.10.1 15:34:41"
    }
    """
    if 'session_id' in request.COOKIES:
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            'session_id': request.COOKIES['session_id'],
            }
        resp = requests.get(url, headers=headers)
        if (resp.status_code >= 200) and (resp.status_code<=300) :
            return render(request, "users/info.html", resp.json())
        else:
            return HttpResponse("err") # отрисовать стр ошибок  

def update(request, question_id):
    if request.method == "POST":
        regist_email = request.POST.get("email")
        regist_password = request.POST.get("password")
        regist_first_name = request.POST.get("first_name")
        regist_last_name = request.POST.get("last_name")
        regist_tel_num = request.POST.get("tel_num")
        regist_about = request.POST.get("about")
        return render(request, "users/otladka.html", {"log": regist_login, "pas": regist_password})
    else:
        # принимает JSON и выводит информацию 
        # пример JSON 
        # ниже пример ( отладочный ) JSON  
        info = {
        "id": 123456,
        "first_name": "Random",
        "last_name": "Valerka",
        "email": "valerka@example.com",
        "tel_num": "1-234-56-78",
        "about": "Some information about this man",
        "time_reg": "2012.10.1 15:34:41"
        }
        return render(request, "users/update.html",info )
