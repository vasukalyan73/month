from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

d={
    'january':' january first month of the year',
    'february':'shortest month on the year',
    'march':'month of exams',
    'april':'month of fools',
    'may':'month of veccation',
    'june':'month of admition',
    'july':'longest month',
    'august':'No Non-veg Month',
    'september':'Ganpathi bappa moreya',
    'otc':'Month of dasara',
    'november':'month of lights',
    'december': None    
}
def index(request):
    l=list(d)
    return render(request,'index.html',{'data':l})
    return HttpResponse(res)


def month_with_num(request,month):
    l=list(d)
    data = l[month-1]
    red_path = reverse('disp',args=[data])
    return HttpResponseRedirect(red_path)
def month(request,month):
    try:
        return render(request,'month.html',{'message':d[month],'m':month})
    except:
        return HttpResponseNotFound('invalied month name ')
        