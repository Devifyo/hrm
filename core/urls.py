from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # This URL is now neutral: /account/redirect/
    path('redirect/', views.global_login_redirect, name='login_redirect'),
]