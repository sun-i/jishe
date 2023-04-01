from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', views.AuthPatientInfo),
    path('login/', views.PatientLogin),
    path('register/', views.PatientRegister),
    path('modify/', views.ModifyInfo)
]
