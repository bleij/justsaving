from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "user/register.html", context)
