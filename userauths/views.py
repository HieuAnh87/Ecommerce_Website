from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
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
