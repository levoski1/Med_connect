from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# View for user registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, f'Email {email} already exists!')
                return redirect('accounts:register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} already exists!')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                return redirect('product:home')
        else:
            messages.error(request, 'Passwords do not match!')
    
    return render(request, "accounts/register.html")

# View for user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
            else:
                request.session.set_expiry(0)  # Browser close session
            return redirect('product:home')
        else:
            messages.error(request, 'Incorrect username or password')
            return redirect('accounts:login')
    
    return render(request, 'accounts/login.html')

# View for user logout
def logout_view(request):
    logout(request)
    return redirect('product:home')
