from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():              
                messages.error(request, f'Email {email} Exist!')
                return redirect('accounts:register')
            elif User.objects.filter(username=username).exists():              
                messages.error(request, f'User {username} Exist!')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                login(request, user)
                return redirect('product:home')
        else:          
            messages.error(request, f'Password Don\'t match')
    return render(request, "accounts/register.html")


# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if remember_me:
                request.session.set_expiry(60 * 2 * 1 * 1)
                return redirect('product:home')
            else:
                request.session.set_expiry(0)
                return redirect('product:home')
        else:
            messages.error(request, f'password or username not correct')
            return redirect('accounts:login')
    else:     
        return render(request, 'accounts/login.html')
    

# logout view

def logout_view(request):
    logout(request)
    return redirect('product:home')