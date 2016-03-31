from django.shortcuts import render
from .models import *
from django.views import generic
from django.core import serializers
import json
# Create your views here.

class represent(generic.TemplateView):
    template_name = "represent.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class article(generic.TemplateView):
    template_name = "article.html"

class MessagePage(generic.TemplateView):
	template_name = "message.html"

class Blog(generic.TemplateView):
	template_name = "blog.html"

class ContactNumbers(generic.TemplateView):
	template_name="contacts.html"

class NitkLifePage(generic.TemplateView):
    template_name = "nitk_life.html"

class SenatePage(generic.TemplateView):
    template_name = "senate.html"

class FAQ(generic.TemplateView):
    template_name="faq.html"

def date_handler(obj):
    # To handle the date format while JSON conversion
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def calEvents(request):
    objectQuerySet = Events.objects.values('id','title','start','end')
    events = json.dumps(list(objectQuerySet), default=date_handler)
    return render(request, 'calendar.html', {'eventlist':events})

def homePage(request):
    eventlist = Events.objects.all().order_by('-start')[:3]
    newslist = News.objects.all().order_by('-timestamp')[:3]
    articlelist = Articles.objects.all().order_by('-published')[:3]
    return render(request,'home.html',{'events':eventlist,'news':newslist,'articles':articlelist})

def announcements(request):
    announcelist = Announcements.objects.all().order_by('timestamp')
    return render(request,'announce.html',{'announcements':announcelist})

def newsPage(request, num=0):
    if num:
        news = News.objects.get(id=num)
        return render(request,'eachNews.html',{'news':news})
    else:
        news = News.objects.all().order_by('timestamp')
        inthenews = news.filter(category='N')
        spotlight = news.filter(category='S')
        campus = news.filter(category='C')
        pinned = news.filter(pinned=True)
        return render(request,'news.html',{'inthenews':inthenews,'spotlight':spotlight,'campus':campus,'pinned':pinned})

def minutes(request):
    minuteslist = Minute.objects.all().order_by('-date_of_meeting')
    return render(request, 'minutes.html', {'minutes':minuteslist})

def mous(request):
    mouslist = MoU.objects.all().order_by('-date_of_signing')
    return render(request, 'mous.html', {'mous':mouslist})

def grants(request):
    grantlist = ResearchGrant.objects.all().order_by('-date_of_grant')
    return render(request, 'grants.html', {'grants':grantlist})

def resources(request):
    resourcelist = Resource.objects.all().order_by('-timestamp')
    return render(request, 'resources.html', {'resources':resourcelist})

def reports(request):
    reportlist = SenateReport.objects.all().order_by('-date_of_report')
    return render(request, 'senatereports.html', {'reports':reportlist})
