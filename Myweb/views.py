from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
        return render(request,"myweb/index.html")
        
def amit(request):
        return HttpResponse("Hello,Amit!")

def greet(request,name):
        return render(request,"myweb/greet.html",{
                "name":name.capitalize()
        })
