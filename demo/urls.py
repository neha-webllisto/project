from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home),
    path('register/',views.register, name="register"),
    path('login/',views.login),
    path('demo/',views.demo,name="dscf"),
]