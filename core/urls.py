
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', include('dashboard.urls')),
    path("auth/", include("django.contrib.auth.urls")),
]
