from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
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
    next_url = req.GET.get('next', None)  

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
        form = UserLoginForm()

    return render(req, 'users/login.html', {'form': form, 'next': next_url})



def logout(req):
    auth_logout(req)
    messages.success(req, "You have been logged out successfully!")
    return render(req, 'users/logout.html')

@login_required
def profile(req):
    if req.method == "POST":
        u_form = UserUpdateForm(req.POST, instance=req.user)
        p_form = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(req, f"Account Updated Successfully!")
            return redirect('users-profile')
        
    else:
        u_form = UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(req, 'users/profile.html', context)
