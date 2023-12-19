from django.urls import path
from app1 import views

urlpatterns = [
    
    path('', views.homePage, name=''),
    path('register', views.registrationPage, name='register'),
    path('login', views.my_loginPage, name='login'),
    path('logout', views.user_logoutPage, name='logout'),
    path('dashboard', views.dashboardPage, name='dashboard'),


]
