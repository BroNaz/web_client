from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import urllib.parse as urlparse
from urllib.parse import urlencode
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

def delete(request,id):
    if 'session_id' in request.COOKIES:
        if request.method == "POST":
            headers['Cookie'] = request.COOKIES['session_id']
            resp = requests.post(url, data=userdata, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                refe = resp.json()
                return redirect(refe["Ref"])
            else:
                return HttpResponse(resp.status_code)
        else:
            resp = requests.get(url, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                return render(request, "ads/update.html", resp.json())
            else:
                return HttpResponse(resp.status_code)
    else:
        return redirect('users/login')

def update(request,id):
    if 'session_id' in request.COOKIES:
        url = 'http://127.0.0.1:8080/ads/'
        url = url+str(id)
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
        }
        resp = requests.get(url, headers=headers)
        if request.method == "POST":
            url = 'http://127.0.0.1:8080/ads/edit/'
            url = url + str(id)
            userdata = {
                'title': request.POST.get("title"),
                'price': request.POST.get("price"),
                'country': request.POST.get("country"),
                'subway_station': request.POST.get("subway_station"),
                'description_ad': request.POST.get("description"),
                'city': request.POST.get("city"),
                }
            headers['Cookie'] = request.COOKIES['session_id']
            resp = requests.post(url, data=userdata, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                refe = resp.json()
                return redirect(refe["Ref"])
            else:
                return HttpResponse(resp.status_code)
        else:
            resp = requests.get(url, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                return render(request, "ads/update.html", resp.json())
            else:
                return HttpResponse(resp.status_code)
    else:
        return redirect('users/login')

def myads(request):
    if 'session_id' in request.COOKIES:
        url = 'http://127.0.0.1:8080/users/profile'
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            'Cookie': request.COOKIES['session_id'],
            }
        resp = requests.get(url, headers=headers)
        if (resp.status_code >= 200) and (resp.status_code<=300) :
            user_id = resp.json()['id']
            url = 'http://127.0.0.1:8080/users/'
            url = url + str(user_id) + '?show_ads=true'
            resp = requests.get(url, headers=headers)
            info = {}
            info['all'] = resp.json()
            return render(request, "ads/myads.html", info )
            #return HttpResponse(user_id)
        else:
            return HttpResponse(resp.status_code)
    else:
         # в случае некорректного session_id
        return redirect('/')

def home_page(request, page = 1):
    if page <= 0:
        page = 1 
    url = 'http://127.0.0.1:8080/ads'
    params = {'limit':10,'offset':(page-1) * 10 }
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    headers = {
        'user-agent': request.META['HTTP_USER_AGENT'],
    }
    resp = requests.get(urlparse.urlunparse(url_parts), headers=headers)
    if resp.status_code<300:
        info = {'count':len(resp.json())}
        i = 0
        while i <  len(resp.json()):
            info[chr(48+i)] = resp.json()[i]
            i = i+1
        return render(request, "ads/home_page2.html", info)
    else:
        return HttpResponse(resp.status_code)


def all_ads(request, id):
    url = 'http://127.0.0.1:8080/users/'
    url = url + str(id) + '?show_ads=true'
    headers = {
        'user-agent': request.META['HTTP_USER_AGENT'],
    }
    resp = requests.get(url, headers=headers)
    if (resp.status_code >= 200) and (resp.status_code<=300) :
        i = 0
        info = {}
        while i <  len(resp.json()):
            info[str(i)] = resp.json()[i]
            i = i+1
        info['all'] = resp.json()
        return render(request, "ads/all_ads.html", info )
    else:
        return HttpResponse(resp.status_code)

def ad(request, id):
    #запрос по id вернуть обьявлние 
    url = 'http://127.0.0.1:8080/ads/'
    url = url+str(id)
    headers = {
        'user-agent': request.META['HTTP_USER_AGENT'],
    }
    resp = requests.get(url, headers=headers)
    if (resp.status_code >= 200) and (resp.status_code<=300) :
        json = resp.json()
        json['creation_time'] = resp.json()['creation_time'][:10]
        return render(request, "ads/ad.html", json)
    else:
        return HttpResponse(resp.status_code)