from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from loginapp.forms import CustomUserCreationForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Login successful!')
            return redirect('movieapp:home')  # Redirect to your home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'loginpage.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginapp:login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registerpage.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('loginapp:login')

def view_profile_modal(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_modal')  # Redirect to the profile modal after successfully editing
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'profile_modal.html', {'user': user, 'form': form})