from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import requests

def new(request):
    if 'session_id' in request.COOKIES:
        if request.method == "POST":
            url = 'http://127.0.0.1:8080/ads/new'
            userdata = {
                'title': request.POST.get("title"),
                'price': request.POST.get("price"),
                'country': request.POST.get("country"),
                'subway_station': request.POST.get("subway_station"),
                'description_ad': request.POST.get("description"),
                'city': request.POST.get("city"),
                }
            headers = {
                'user-agent': request.META['HTTP_USER_AGENT'],
                'Cookie': request.COOKIES['session_id'],
                }
            resp = requests.post(url, data=userdata, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                refe = resp.json()
                return redirect(refe["Ref"])
            else:
                return HttpResponse(resp.status_code)
        else:
            return render(request, "ads/new.html")
    else:
        return redirect('users/login')

def delete(request,question_id):
    return render(request, "ads/delete.html")

def home_page(request, page = 1):
    url = 'http://127.0.0.1:8080/ads'
    headers = {
        'user-agent': request.META['HTTP_USER_AGENT'],
    }
    userdata = {
                'offset': 100 ,
                'limit': 10,
            }
    resp = requests.get(url, headers=headers, data=userdata)
    if resp.status_code<300:
        info = {'count':len(resp.json())}
        i = 0
        while i <  len(resp.json()):
            info[chr(48+i)] = resp.json()[i]
            i = i+1
        #info = {'object': resp., 'count': len(resp.json())}
        #return HttpResponse(resp.json()[0])
        return render(request, "ads/home_page2.html", info)
    else:
        return HttpResponse(resp.status_code)
    #не забыть об искусственном внесение счетчика !
    #return render(request, "ads/home_page2.html", info)

def update(request, question_id):
    return render(request, "ads/update.html")

def ad(request, id, id_ad):
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