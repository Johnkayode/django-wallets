from django.shortcuts import redirect, render

from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            return redirect("register")
        else:
            return render(request, "accounts/register.html", context = {"form":form})
    return render(request, "accounts/register.html", context = {"form":form})