from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("register/", views.SignUpView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name='login'),
    path('profile/', views.TemplateView.as_view(), name='profile')

]
