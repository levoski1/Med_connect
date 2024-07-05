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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
