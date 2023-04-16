from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Insert_topic(request):
    if request.method=='POST':
        IT=request.POST['topic']
        TO=Topic.objects.create(Topic_name=IT)
        TO.save()
        return HttpResponse('inserted topic into topic model')

    return render(request,'insert_topic.html')

def Insert_webpage(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    if request.method=='POST':
        TN=request.POST['topic']
        NA=request.POST['name']
        UR=request.POST['url']
        EM=request.POST['email']
        To=Topic.objects.get(Topic_name=TN)
        WO=Webpages.objects.create(Topic_name=To,Name=NA,URL=UR,Email=EM)
        WO.save()
        return HttpResponse(f'inserted data into webpages under{To.Topic_name} ')
    return render(request, 'insert_webpages.html',d)
def display_webpages(request):
    WO=Webpages.objects.all()
    d={'webpages':WO}
    return render(request,'display_webpages.html',d)

def retrive_webpages(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    if request.method=='POST':
        gt=request.POST.getlist('topic_name')
        emptyQset=Webpages.objects.none()
        for i in gt:
            emptyQset=emptyQset | Webpages.objects.filter(Topic_name=i)
        d1={'webpages':emptyQset}
        return render(request,'retrive_webpages.html',d1)
    return render(request,'display_topics.html',d)
def retrive_web_checkbox(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    return render(request,'retrive_web_checkbox.html',d)

def retrive_web_radio(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    return render(request,'retrive_web_radio.html',d)
