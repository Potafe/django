from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = "users-register"),
    path('login/', views.login, name = "users-login"),
    path('logout/', views.logout, name = "users-logout"),
    path('profile/', views.profile, name = "users-profile")
]
