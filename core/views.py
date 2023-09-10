from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django import views
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "index.html"

class DashboardView(views.View):
    template_name = 'profile.html'
    def get(self, request, *args, **kwargs):
        return render(request, template_name)

    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class SignUp(views.View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

class LoginView(views.View):
    def get(self, request, *args , **kwargs):
        return render(request, 'login.html')
        
    
