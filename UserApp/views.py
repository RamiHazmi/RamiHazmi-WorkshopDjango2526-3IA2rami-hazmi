from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import logout
# Create your views here.

def register(req):
    if req.method =="POST":
        form =UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form =UserRegisterForm()
        return render(req, 'register.html', {"form":form})
    return render(req, 'register.html', {"form":form})

def logout_view(req):
    logout(req)
    return redirect("login")