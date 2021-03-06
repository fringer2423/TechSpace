from .services.auth_service import get_user, EventAuth

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            user = get_user(EventAuth.LOGIN, form)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Неверные учетные данные'
        else:
            msg = 'Ошибка при проверке формы'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user_view(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = get_user(EventAuth.REGISTER, form)

            msg = f'Вы зарегистрированы. Пожалуйста, <a href="/login">войдите</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Ошибка при проверке формы'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
