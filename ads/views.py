from django.shortcuts import render
import requests

def new(request):
    if request.method == "POST":
        url = 'http..' # url - для POST отправки
        userdata = {
            'title': request.POST.get("title"),
            'price': request.POST.get("price"),
            'country': request.POST.get("country"),
            'subway_station': request.POST.get("subway_station"),
            'description': request.POST.get("description"),
            'city': request.POST.get("city"),
            }
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            'session_id': 'id......',
            }
        resp = requests.post(url, data=userdata, headers=headers)
        return render(request, "users/otladka.html", userdata)
        #в место отладочных полей 
        #будет отправка POST запроса на сервер 
        #и ожидания ответа в формате JSON 
        #return HttpResponseRedirect("/ads")
    else:
        return render(request, "ads/new.html")

def delete(request,question_id):
    return render(request, "ads/delete.html")

def home_page(request, question_id = 1):
    #пока что хардкод 
    info = {
        "info1" :
            {
            "id": 1111,
            "title": "My awesome title",
            "price": 11111111,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 11111111111,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info2" :
            {
            "id": 222222,
            "title": "My awesome title",
            "price": 2222222222,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 22222222222,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info3" :
            {
            "id": 3333333333,
            "title": "My awesome title",
            "price": 33333333333,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 3333333333,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info4" :
            {
            "id": 4444444,
            "title": "My awesome title",
            "price": 4444444444,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 4444444444444,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info5" :
            {
            "id": 55555,
            "title": "My awesome title",
            "price": 55555555,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 555555555555,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info6" :
            {
            "id": 66666666666,
            "title": "My awesome title",
            "price": 666666666666,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 666666666666,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info7" :
            {
            "id": 777777777,
            "title": "My awesome title",
            "price": 777777,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 777777,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info8" :
            {
            "id": 88888,
            "title": "My awesome title",
            "price": 88888,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 88888,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info9" :
            {
            "id": 999999,
            "title": "My awesome title",
            "price": 999999,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 999999,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "info10" :
            {
            "id": 10101010,
            "title": "My awesome title",
            "price": 10101010,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 10101010,
                "first_name": "Random",
                "last name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            },
        "count": 10, 
        }
    #не забыть об искусственном внесение счетчика !
    return render(request, "ads/home_page2.html", info)

def update(request, question_id):
    return render(request, "ads/update.html")

def ad(request, question_id):
    #запрос по id вернуть обьявлние 
    info = {
            "id": 1111,
            "title": "My awesome title",
            "price": 11111111,
            "country": "Russia",
            "city": "Moscow",
            "subway_station": "Technopark",
            "images_url": ["ex.com/ad_id/1.png", "ex.com/ad_id/2.png"],
            "agent_info": 
                {
                "id": 11111111111,
                "first_name": "Random",
                "last_name": "Valerka",
                "email": "valerka@example.com",
                "tel_num": "1-234-56-78",
                "about": "Some information about this man",
                "time_reg": "2012.10.1 15:34:41"
                },
            "description": "it is awesome service with the best quality!",
            "time_cre": "2012.10.1 15:40:52"
            }
    return render(request, "ads/ad.html", info)