from django.shortcuts import render, redirect
# third party imports
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# import within
from .forms import CreateUserForm 



# Create your views here.


# register
def registerPage(request):
    form = CreateUserForm ()

    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'users/register.html', context)

# LOGIN
def loginPage(request):
    form = UserCreationForm()

    context = {'form':form}
    return render(request, 'users/login.html', context)























def index(request):
    return render(request, 'users/index.html')