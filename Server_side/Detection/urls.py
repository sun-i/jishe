from django.contrib import admin
from django.urls import path, include
import Detection.views as views

urlpatterns = [
    path('load/', views.load_image),
    path('download/', views.DownloadFile),
    path('reportword/', views.GenerateReportWord),
    path('medicword/', views.GenerateMedicWord)
]
