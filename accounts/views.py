from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    context={}

    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Bienvenue !")

        else:

            context["errors"]=form.errors

    form = UserCreationForm()
    context["form"]=form

    return render(request,"accounts/signup.html",context)