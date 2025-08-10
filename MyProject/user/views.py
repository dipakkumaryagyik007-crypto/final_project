from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    data = notice.objects.all()[0:4]
    d = {"ndata": data}
    return render(request, "index.html", d)


def contact(request):
    d={}
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("email")
        c=request.POST.get("mob")
        e=request.POST.get("msg")
       # d={"x1":name,"x2":email,"x3":mobile,"x4":massage}
        contactus(name=a,mobile=c,email=b,massage=e).save()
        return HttpResponse("<script>alert('data added successfully..');location.href='/contact/';</script>")
    return render(request,"contact.html")

def gallery(request):
    data=igallery.objects.all()
    d={"gdata":data}
    return render(request,"gallery.html",d)

def wchoose(request):
    return render(request,"wchoose.html")

def team(request):
    data=ourfaculty.objects.all()
    d={"fdata":data}

    return render(request,"team.html",d)

def about(request):
    return render(request,"about.html")

# Login view
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            return HttpResponse("<script>alert('Invalid credentials');location.href='/';</script>")
    return HttpResponse("<script>alert('Invalid request');location.href='/';</script>")

# Signup view
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=email).exists():
            return HttpResponse("<script>alert('Email already registered');location.href='/';</script>")
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        return HttpResponse("<script>alert('Signup successful! Please login.');location.href='/';</script>")
    return HttpResponse("<script>alert('Invalid request');location.href='/';</script>")

def details(request):
    return render(request,"details.html")

def facilities(request):
    data=myfacilities.objects.all()
    d={"gdata":data}
    return render(request,"facilities.html",d)

def placement(request):
    data=ourplacement.objects.all()
    d={"pdata":data}
    return render(request,"placement.html",d)

def course(request):
    data=mycourse.objects.all()
    d={"cdata":data}
    return render(request,"course.html",d)