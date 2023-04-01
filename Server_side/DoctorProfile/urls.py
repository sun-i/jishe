from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', views.AuthDoctorInfo),
    path('login/', views.DoctorLogin),
    path('register/', views.DoctorRegister),
    path('modify/', views.ModifyInfo),
    path('all/', views.GetAllDoctors)
]
