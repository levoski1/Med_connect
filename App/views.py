from django.shortcuts import render, redirect
from App.forms import RegisterForm, PrescriptionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from App.models import PrescriptionModel


# Create your views here.

def home(request):
    return render(request, 'app/home.html')



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)          
            return redirect('login')
    else:
         form = RegisterForm()
    return render(request, "app/register.html", {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('upload_prescription')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})
    


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def upload_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.user = request.user
            prescription.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'app/prescription.html', {'form':form})

@login_required
def prescription_list(request):
    if request.method == 'POST':
        prescriptions = PrescriptionModel.objects.filter(user=request.user)
        return render(request, 'app/prescription_list.html', {'prescriptions': prescriptions})
    else:
        prescriptions = PrescriptionModel.objects.filter(user=request.user)
        return render(request, 'app/prescription_list.html', {'prescriptions': prescriptions})
