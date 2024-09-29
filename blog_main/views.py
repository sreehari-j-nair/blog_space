from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from . models import Posts
from . import models

# Create your views here.
def signup(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("confirm_password")

        if password != c_password:
            messages.error(request,"Password mismatch!!!")
            return redirect("signup")
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already registered!!")
            return redirect("signup")
        
        user = User.objects.create_user(name,email,c_password)
        user.save()

        messages.success(request,"User registered successfully!!")
        return redirect("signin")

    return render (request,"signup.html")

def signin(request):

    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(request,username = name,password=password)

        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("signin")

    return render(request,"signin.html")

def homepage(request):

    context = {"posts":Posts.objects.all().order_by('-date')}
    return render(request,"homepage.html", context)

def newpost(request):

    if request.method == "POST":
        title = request.POST.get("heading")
        content =request.POST.get("content")

        new_post = models.Posts(title = title, content = content, author = request.user)
        new_post.save()
        return redirect("homepage")
    
    return render(request,"new_post.html")

def profile(request):

    context = {"posts":Posts.objects.filter(author=request.user).order_by('-date')}
    return render(request,"profile_page.html",context)

def signout(request):
    logout(request)
    return redirect("signin")