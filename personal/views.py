from django.shortcuts import render
from  . import models


# Create your views here.
def index(request):
    aboutme = models.aboutme.objects.all()
    servises = models.servises.objects.all()
    servises1 = models.servises1.objects.all()
    servises2 = models.servises2.objects.all()
    servises3 = models.servises3.objects.all()
    servises4 = models.servises4.objects.all()
    servises5 = models.servises5.objects.all()
    more = models.more.objects.all()
    more1 = models.more1.objects.all()
    more2 = models.more2.objects.all()
    more3 = models.more3.objects.all()
    work_sample = models.Work_samples.objects.all()
    work_sample1 = models.Work_samples1.objects.all()
    ostads = models.ostads.objects.all()
    return render(request,'personal/index.html',context={'aboutme':aboutme,'servises':servises,'servises1':servises1,'servises2':servises2,'servises3':servises3,'servises4':servises4,'servises5':servises5,'more':more,'more1':more1,'more2':more2,'more3':more3,'work_sample':work_sample,'work_sample1':work_sample1,'ostads':ostads})


def blog(request):
    return render(request,'personal/blogs-page.html')