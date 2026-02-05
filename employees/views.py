from multiprocessing import context
from urllib import request
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    # Later you can pass context like 'total_leaves': 12
    return render(request, 'dashboard.html') 