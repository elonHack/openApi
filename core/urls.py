from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("profile/", views.DashboardView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.SignUp.as_view(), name='create')

]
