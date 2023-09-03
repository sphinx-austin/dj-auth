from django.shortcuts import render, redirect
# third party imports
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm




# Create your views here.


# register
def registerPage(request):
    form = UserCreationForm()

    context = {'form':form}
    return render(request, 'users/register.html', context)

# LOGIN
def loginPage(request):
    form = UserCreationForm()

    context = {'form':form}
    return render(request, 'users/login.html', context)























def index(request):
    return render(request, 'users/index.html')