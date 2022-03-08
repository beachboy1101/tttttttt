from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import random

# Create your views here.
def sayhello(request):
    return HttpResponse('hello django!')

def hello2(request,username):
    return HttpResponse("hello" + username)

def hello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())

def hello4(request,username):
    now = datetime.now()
    return render(request,"hello4.html",locals())

def dice(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    no4 = random.randint(1,6)
    return render(request,'dice.html',locals())