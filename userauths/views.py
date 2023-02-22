from django.contrib import messages
from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from .models import User


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        # Check if the form is valid
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            print("User registered")
            return redirect("core:index")
    else:
        print("User can not register")
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "userauths/sign-up.html", context)


def login_view(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("core:index")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Check if the user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with email {email} does not exist")
            return redirect("userauths:login")
        # Check if the user is authenticated
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {user.username}")
            return redirect("core:index")
        else:
            messages.warning(request, "Email or password is incorrect")
    context = {}
    return render(request, "userauths/sign-in.html", context)

