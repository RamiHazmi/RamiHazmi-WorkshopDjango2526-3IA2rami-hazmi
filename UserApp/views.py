from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(req):
    if req.method == "POST":
        form =UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form =UserRegisterForm()
        return render(req, 'register.html' ,{"form":form})






# Create your views here.
