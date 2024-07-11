from django.contrib.auth import views as my_views
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from App.forms import PrescriptionForm
from django.contrib.auth.decorators import login_required
from App.models import PrescriptionModel




# upload view
@login_required
def upload_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.user = request.user
            prescription.save()
            return redirect('app:prescription')
    else:
        form = PrescriptionForm()
    return render(request, 'app/prescription.html', {'form':form})

# Drug view
@login_required
def prescription_list(request):
    if request.method == 'POST':
        prescriptions = PrescriptionModel.objects.filter(user=request.user)
        return render(request, 'app/prescription_list.html', {'prescriptions': prescriptions})
    else:
        prescriptions = PrescriptionModel.objects.filter(user=request.user)
        return render(request, 'app/prescription_list.html', {'prescriptions': prescriptions})



# Password reset
class forget_password(my_views.PasswordResetView):
    template_name = 'app/forget_password.html'
    token_generator = default_token_generator


class PasswordResetDone(my_views.PasswordResetDoneView):
    template_name = 'app/reset_done.html'


class PasswordResetConfirm(my_views.PasswordResetConfirmView):
    template_name = 'app/reset_confirm.html'


class PasswordResetComplete(my_views.PasswordResetCompleteView):
    template_name = 'app/reset_complete.html'




# Register view
# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Registration successful. Welcome to MedConnect!')
#             user = form.save()
#             login(request, user)                   
#             return redirect('product:home')
#         else:
#             for field, error in form.errors.items():
#                 for error in error:
#                     messages.error(request, f'Error in {field} : {error}')
#     form = RegisterForm()
#     return render(request, "app/register.html", {'form': form})


# # login view
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             remember_me = request.POST.get('remember_me')
#             user = authenticate(username=username, password = password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Login successful. Welcome to MedConnect!')
#                 if remember_me:
#                     request.session.set_expiry(60 * 2 * 1 * 1)
#                 else:
#                     request.session.set_expiry(0)
            
#                 return redirect('product:home')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f'Error in {field} : {error}')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'app/login.html', {'form': form})
    

# # logout view

# def logout_view(request):
#     logout(request)
#     return redirect('product:home')