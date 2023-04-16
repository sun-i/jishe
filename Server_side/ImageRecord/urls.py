from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.UploadImage),
    path('read/', views.ReadImage)
]