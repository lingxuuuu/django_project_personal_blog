from django.contrib import admin
from django.urls import path, include
#code below is important to understand in case to understand the--
#--user_views.register and auth_views.LoginView 
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)