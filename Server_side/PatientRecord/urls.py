from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('list/<int:id>/', views.GetAllPatientRecordByDoctorId),
    path('<int:id>/', views.GetPatientRecordByRecordId),
    path('list/patient/<int:id>/', views.GetAllPatientRecordByPatientId),
    path('all/', views.GetAllPatientRecord),
    path('create/', views.AddPatientRecord),
    path('uncheck/<int:id>/', views.GetUnCheckedRecordByDoctorId)
]