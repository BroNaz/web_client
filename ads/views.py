# -*- coding: utf-8 -*-

"""
  Module control for application "ads"
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import urllib.parse as urlparse
from urllib.parse import urlencode
import requests


# base url database
url_root = 'https://search-build.herokuapp.com'



def new(request):
    """
    def new(request)
     Submission of new advertisement function.

    in the case of a post request, forwards the fields from the template "ads/new.html" title, price, country, subway_station, description, city  to the database
    only works with session_id
    with a successful response redirect to the page of the advertisement

    Args:
    request : request, cleaned stores the information about the session

    """
    if 'session_id' in request.COOKIES:
        if request.method == "POST":
            url = url_root + '/ads/new'
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
                object_err = resp.json()
                object_err['status'] = resp.status_code
                return render(request, "errors.html",  object_err)
        else:
            return render(request, "ads/new.html")
    else:
        return redirect('/users/login/')



def delete(request,id):
    """
    Ad delete feature
    cookies are checked for valid data, the advertisement is deleted

    Args:
        request : request, cleaned stores the information about the session
        id(int) : delete advertisement id
        
    """
    if 'session_id' in request.COOKIES:
        if request.method == "POST":
            url = url_root + '/ads/delete/'
            url = url+str(id)
            headers = {
                'user-agent': request.META['HTTP_USER_AGENT'],
                'Cookie': request.COOKIES['session_id'],
                }
            resp = requests.delete(url, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                return redirect('/ads/myads/')
            else:
                object_err = resp.json()
                object_err['status'] = resp.status_code
                return render(request, "errors.html",  object_err)
        else:
            info = { 'id' : id }
            return render(request, 'ads/delete.html', info)
    else:
        return redirect('/users/login/')



def update(request,id):
    """
    Ad delete feature

    cookies are checked for valid data, the announcements is update
    during the POST request, all the same fields are sent as in the "new_ads" function, which are taken from the template "ads/update.html"

    Args:
        request : request, cleaned stores the information about the session
        id(int) : update advertisement id
    """

    if 'session_id' in request.COOKIES:
        url = url_root + '/ads/'
        url = url+str(id)
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
        }
        resp = requests.get(url, headers=headers)
        if request.method == "POST":
            url = url_root +'/ads/edit/'
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
                object_err = resp.json()
                object_err['status'] = resp.status_code
                return render(request, "errors.html",  object_err)
        else:
            resp = requests.get(url, headers=headers)
            if (resp.status_code >= 200) and (resp.status_code<=300) :
                return render(request, "ads/update.html", resp.json())
            else:
                object_err = resp.json()
                object_err['status'] = resp.status_code
                return render(request, "errors.html",  object_err)
    else:
        return redirect('/users/login/')


def myads(request):
    """
    function that returns all user declaration
    Cookies are checked for the accuracy of the data; in case of success, all ads are displayed.
    template is used "ads/myads.html"

    Args:
        request : request, cleaned stores the information about the session

    """

    if 'session_id' in request.COOKIES:
        url = url_root + '/users/profile'
        headers = {
            'user-agent': request.META['HTTP_USER_AGENT'],
            'Cookie': request.COOKIES['session_id'],
            }
        resp = requests.get(url, headers=headers)
        if (resp.status_code >= 200) and (resp.status_code<=300) :
            user_id = resp.json()['id']
            url = url_root + '/users/'
            url = url + str(user_id) + '?show_ads=true'
            resp = requests.get(url, headers=headers)
            info = {}
            info['all'] = resp.json()
            return render(request, "ads/myads.html", info )
        else:
            object_err = resp.json()
            object_err['status'] = resp.status_code
            return render(request, "errors.html",  object_err)
    else:
        return redirect('/')

 
def home_page(request, page = 1, search = ''):
    """
    The main function of the withdrawal of ads

    
    template is used "ads/home_page2.html"

    Args:
        request : request, cleaned stores the information about the session
        id(int) : To coordinate ad numbers that output
        search(str) : To display ads on request in search

    """
    if search != '' and bool(request.GET.get("search")):
        page = 1 
    if page <= 0:
        page = 1 
    url = url_root + '/ads'
    params = {'limit':10,'offset':(page-1) * 10 }
    if bool(request.GET.get("search")):
        params['query'] = request.GET.get("search")
    if search != '':
        params['query'] = search
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
        info['page_next'] = page+1
        info['page_last'] = page-1
        if bool(request.GET.get("search")):
            info['search'] = request.GET.get("search")
        elif search != '':
            info['search'] = search 
        else :
            info['search'] = 'search'
        i = 0
        while i <  len(resp.json()):
            info[chr(48+i)] = resp.json()[i]
            image = info[chr(48+i)]["ad_images"]
            if not image:
                info[chr(48+i)]['image0'] = "https://www.layoutit.com/img/sports-q-c-1600-500-1.jpg"
                info[chr(48+i)]['image1'] = "https://www.layoutit.com/img/sports-q-c-1600-500-2.jpg"
                info[chr(48+i)]['image2'] = "https://www.layoutit.com/img/sports-q-c-1600-500-3.jpg"
                info[chr(48+i)]['image_count'] = 3
            else:
                k = 0
                for j in image:
                    info[chr(48+i)]['image' + str(k)] = j
                    k = k + 1
                info[chr(48+i)]['image_count'] = len(image)
            if info[chr(48+i)]['image_count'] == 1:
                info[chr(48+i)]['image1'] = info[chr(48+i)]['image2'] = info[chr(48+i)]['image0']
            if info[chr(48+i)]['image_count'] == 2:
                info[chr(48+i)]['image2'] = info[chr(48+i)]['image0']
            i = i + 1
        return render(request, "ads/home_page2.html", info)
        #return HttpResponse(resp.text)
    else:
        object_err = resp.json()
        object_err['status'] = resp.status_code
        return render(request, "errors.html",  object_err)
        


def all_ads(request, id):
    """
    output function of all all user ads (without access to editing)
    template is used "ads/ad.html"

    Args:
        request : request, cleaned stores the information about the session
        id(int) : user id whose ads are displayed
    """
    url = url_root + '/users/'
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
        object_err = resp.json()
        object_err['status'] = resp.status_code
        return render(request, "errors.html",  object_err)

def ad(request, id):
    """
    the function to display all user ads (without access to editing)

    template is used "ads/ad.html"
    the function to display all user ads (without access to editing)

    Args:
        request : request, cleaned stores the information about the session
        id(int) : id advertisement which is displayed

    """
    url = url_root + '/ads/'
    url = url+str(id)
    headers = {
        'user-agent': request.META['HTTP_USER_AGENT'],
    }
    resp = requests.get(url, headers=headers)
    if (resp.status_code >= 200) and (resp.status_code<=300) :
        json = resp.json()
        json['creation_time'] = resp.json()['creation_time'][:10]
        ad_images = resp.json()['ad_images']
        k = 0 
        for a in ad_images:
            json['ad_images'+str(k)] = a
            k = k + 1
        if len(resp.json()['ad_images']) == 0:
                json['ad_images0'] = "https://www.layoutit.com/img/sports-q-c-1600-500-1.jpg"
                json['ad_images1'] = "https://www.layoutit.com/img/sports-q-c-1600-500-2.jpg"
                json['ad_images2'] = "https://www.layoutit.com/img/sports-q-c-1600-500-3.jpg"
        if len(resp.json()['ad_images']) == 1:
            json['ad_images1'] = json['ad_images2'] = json['ad_images0']
        if len(resp.json()['ad_images']) == 2:
            json['ad_images2'] = json['ad_images0']
        return render(request, "ads/ad.html", json)
        #return HttpResponse(resp.text)
    else:
        object_err = resp.json()
        object_err['status'] = resp.status_code
        return render(request, "errors.html",  object_err)