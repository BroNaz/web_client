from django.shortcuts import HttpResponse
from django.views import generic



def ads(request):
    return HttpResponse("вывисти 10 сообщений ")


def after_ads(request , val ):
    if val == 'new' :
        return HttpResponse("")
    elif val.isdigit : 
        return HttpResponse("")
    else :
        return HttpResponse("")