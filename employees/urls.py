from django.urls import path
from . import views

app_name = 'employees'  # <--- This is the namespace

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('attendance/',views.attendance,name='attendance'),
]