# Create your views here.
from models import Comic
from django.shortcuts import render_to_response, redirect
import random

def lastcomic(request):
    comic = Comic.objects.order_by('-number')[0]
    return render_to_response('comic.html', locals())

def randomcomic(request):
    latestcomic = Comic.objects.order_by('-number')[0]
    randomnumber = random.randint(1, latestcomic.number)
    return redirect('particular', unicode(randomnumber))

def particularcomic(request, number):
    comic = Comic.objects.get(number=int(number))
    return render_to_response('comic.html', locals())

def previouscomic(request, number):
    if number == u'1':
        return redirect('particular', u'1')
    return redirect('particular', unicode(int(number) - 1))

def nextcomic(request, number):
    if number == unicode(Comic.objects.order_by('-number')[0].number):
        return redirect('particular', unicode(Comic.objects.order_by('-number')[0].number))
    return redirect('particular', unicode(int(number) + 1))