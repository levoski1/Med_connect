from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'app'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('prescription/', views.upload_prescription, name='upload_prescription'),
    path('prescription_list/', views.prescription_list, name='prescription'),

    path('password_reset/', views.forget_password.as_view(), name='forget_password'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)