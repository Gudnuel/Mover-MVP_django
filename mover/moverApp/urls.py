from django.urls import path
from .views import SignUpPage,LoginPage,DashBoard,logoutUser


# app_name="mover"
urlpatterns=[
    path('signup/',SignUpPage, name="signUpPage"),
    path('login/', LoginPage, name="loginPage"),
    path('logoutUser/', logoutUser, name="logoutUser"),
    path('dashboard/',DashBoard, name="Dashboard")
]