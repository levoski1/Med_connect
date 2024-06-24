from django.urls import path
from App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout, name='logout'),    
]