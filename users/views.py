from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import registration

# На данном этапе реализации отладка ведется через 
# внутренние поля (смотреть файл models.py в соответствующей директории),
# в дальнейшей реализации ожидается связь с серверной частью 

def delete(request, question_id):
    return render(request, "users/delete.html")
"""
def create(request):
    if request.method == "POST":
        regist = registration()
        regist.login = request.POST.get("login")
        regist.password = request.POST.get("password")
        regist.save()
    return HttpResponseRedirect("/")"""

def new_users(request):
    if request.method == "POST":
        #regist = registration()
        regist_email = request.POST.get("email")
        regist_password = request.POST.get("password")
        regist_first_name = request.POST.get("first_name")
        regist_last_name = request.POST.get("last_name")
        regist_tel_num = request.POST.get("tel_num")
        regist_about = request.POST.get("about")
        return render(request, "users/otladka.html", {"log": regist_email, "pas": regist_password, "fnam" : regist_first_name, 
        "lnam": regist_last_name, "tel": regist_tel_num, "about":regist_about})
        ##########regist.save()
        #в место отладочных полей 
        #будет отправка POST запроса на сервер 
        #и ожидания ответа в формате JSON 
        #return HttpResponseRedirect("/ads")
    else:
        #regist = registration.objects.all()
        return render(request, "users/new_users.html", )

def info(request, question_id):
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
    return render(request, "users/info.html", info)

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
