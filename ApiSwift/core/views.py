from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth
from django import http, views
from .forms import CreateUserForm, LoginForm
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


def home_view(request):
    return render(request, 'core/index.html')

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile')
        
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            Token.objects.create(user=request.user).save()
            form.save()
            return redirect('login')
    return render(request, 'core/signup.html', {'form':form})

@csrf_exempt
def obtain_api_token(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated, generate or retrieve an API token
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required(login_url='login')
def profile_veiw(request):
    key,error = Token.objects.get_or_create(user=request.user)
    return render(request, 'core/profile.html', {"key":key})

