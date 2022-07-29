from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login_user(request):
    context = {}
    page = 'login'
    context['page'] = page
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('polls_list')

    return render(request, 'accounts/login_register.html', context )


def logout_user(request):
    auth.logout(request)
    return redirect('login_page')


def register_user(request):
    page = 'register'
    context = {}
    form = UserCreationForm()
    context['form'] = form
    context['page'] = page
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(
                request,
                username=user.username, password=request.POST['password1']
            )
            if user is not None:
                login(request, user)
                return redirect('polls_list')
    return render(request, 'accounts/login_register.html', context)
