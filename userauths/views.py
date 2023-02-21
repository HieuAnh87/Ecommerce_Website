from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')

            print("User registered")
    else:
        print("User can not register")
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, "userauths/sign-up.html", context)
