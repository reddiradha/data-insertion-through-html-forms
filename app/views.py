from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        To.save()
        return HttpResponse('Topic is inserted successfully')
        
        
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST.get('n')
        url=request.POST.get('url')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('webpage is inserted successfully')
    return render(request,'insert_webpage.html',d)
    
def insert_access(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}
    if request.method=='POST':
        name=request.POST.get('n')
        author=request.POST.get('a')
        date=request.POST.get('date')
        W=Webpage.objects.get_or_create(name=name)[0]
        W.save()
        A=Accessrecord.objects.get_or_create(name=W,author=author,date=date)[0]
        A.save()
        return HttpResponse('accessrecords is inserted successfully')
    return render(request,'insert_access.html',d)
    