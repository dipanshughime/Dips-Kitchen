import email
from re import sub
from datetime import datetime
from django.shortcuts import render, HttpResponse,redirect
from home.models import Contacts
from django.contrib.auth.models import User

# Create your views here
def index(request):
  #context = {
  #  "variable" : "this is text"
  #}
 # return render(request,'index.html',context) 
  return render(request,'index.html')
  #return HttpResponse('this is home page')

def about(request):
  return render(request,'about.html')
  #return HttpResponse('this is about about')

def services(request):
  return render(request,'services.html')
  #return HttpResponse('this is services page')

def offers(request):
  return render(request,'offers.html')

  #return HttpResponse('this is offer wala page')
def login(request):
  if request.method=="POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username='username', password='password')

    if user is not None:
    # A backend authenticated the credentials
       return redirect("/")

    else:
    # No backend authenticated the credentials
        return render(request,'login.html')

  return render(request,'login.html')

def logout(request):
  return render(request,'index.html')

def contacts(request):
  if request.method =="POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc') 
    contacts = Contacts(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
    contacts.save()




  return render(request,'contacts.html')
  #return HttpResponse('this is contact page')
