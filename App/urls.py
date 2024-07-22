from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'app'
urlpatterns = [
    path('',views.landing_page, name='landing'),
    path('prescription/', views.upload_prescription, name='upload_prescription'),
    path('prescription_list/', views.prescription_list, name='prescription'),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
