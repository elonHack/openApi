from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth
from django import http, views
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView


class HomeView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    

class SignUpView(CreateView):
    template_name = 'signup.html'
    model = User
    fields = ["username", "email", "password"]
    success_url = reverse_lazy("home")

class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
    
        # Authenticate user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')  # Replace 'home' with the URL name of your home page
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})

class ProfileView(TemplateView):
    template_name = 'profile.html'
