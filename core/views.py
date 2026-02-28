from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def global_login_redirect(request):
    user = request.user

    # 1. Super Admin
    if user.is_superuser:
        return redirect('/admin/')
    
    # 2. CEO / Executives (Example of a future dedicated app)
    elif user.groups.filter(name='CEO').exists():
        # Assuming you create an 'executive' app later
        #return redirect('executive:dashboard') 
        return redirect('/admin/')
        
    # 3. Managers / HR
    elif user.groups.filter(name='Manager').exists():
        return redirect('employees:manager_dashboard')
    
    # 4. Standard Employees (Default Fallback)
    else:
        return redirect('employees:dashboard')