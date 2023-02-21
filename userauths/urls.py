from django.urls import path

from userauths.views import register

app_name = "userauths"

urlpatterns = [
    path("sign-up/", register, name="sign-up"),
]
