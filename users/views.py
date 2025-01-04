from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm, UserLoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(req):
    if req.method == "POST":
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(req, f"Account created successfully for User {username}!")
            return redirect('users-login')
    else:
        form = UserRegisterForm()
        
    return render(req, 'users/register.html', {'form': form})


def login(req):
    if req.method == "POST":
        form = UserLoginForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(req, user)

            next_url = req.POST.get('next', None)
            if next_url:
                return redirect(next_url)  
            
            messages.success(req, f"Welcome back, {user.username}!")
            return redirect('blog-home')
        else:
            messages.error(req, "Invalid username or password.")
    else:
        next_url = req.GET.get('next', None)
        form = UserLoginForm()
        
    return render(req, 'users/login.html', {'form': form, 'next': next_url})


def logout(req):
    auth_logout(req)
    messages.success(req, "You have been logged out successfully!")
    return render(req, 'users/logout.html')

@login_required
def profile(req):
    return render(req, 'users/profile.html')
