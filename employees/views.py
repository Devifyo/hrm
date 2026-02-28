from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import date, timedelta
import random




def dashboard(request):
    # Later you can pass context like 'total_leaves': 12
    return render(request, 'dashboard.html') 


def attendance(request):
    today = date.today()
    records = []

    for i in range(30):
        day = today - timedelta(days=i)
        status = random.choice(["present", "late", "leave", "half", "absent"])
        shift_type = random.choice(["Day Shift", "Night Shift"])

        if status == "present":
            progress = random.randint(75, 100)
            production = "8h 25m"
            break_hours = "0h 50m"
            overtime = "0h 15m"
            total_hours = "9h 30m"
            clock_in = "09:03 AM"
            clock_out = "06:50 PM"
            leave_type = None
            approval = "Approved"

        elif status == "late":
            progress = random.randint(40, 69)
            production = "8h 10m"
            break_hours = "0h 55m"
            overtime = "0h 00m"
            total_hours = "9h 05m"
            clock_in = "09:45 AM"
            clock_out = "07:30 PM"
            leave_type = None
            approval = "Approved"

        elif status == "half":
            progress = random.randint(30, 50)
            production = "3h 30m"
            break_hours = "0h 15m"
            overtime = "--"
            total_hours = "3h 45m"
            clock_in = "09:40 AM"
            clock_out = "01:15 PM"
            leave_type = None
            approval = "Pending"

        elif status == "leave":
            progress = 0
            production = "--"
            break_hours = "--"
            overtime = "--"
            total_hours = "--"
            clock_in = "--"
            clock_out = "--"
            leave_type = "Sick Leave"   # will show badge
            approval = "Approved"


        else:  # absent
            progress = 0
            production = "--"
            break_hours = "--"
            overtime = "--"
            total_hours = "--"
            clock_in = "--"
            clock_out = "--"
            leave_type = None
            approval = "Rejected"

        records.append({
            "date": day,
            "status": status,
            "shift_type": shift_type if status != "leave" and status != "absent" else "--",
            "clock_in": clock_in,
            "clock_out": clock_out,
            "production_hours": production,
            "break_hours": break_hours,
            "overtime": overtime,
            "progress": progress,
            "total_hours": total_hours,
            "leave_type": leave_type,
            "approval_status": approval,
        })

    paginator = Paginator(records, 20)
    page_obj = paginator.get_page(request.GET.get("page", 1))

    return render(request, "attendance.html", {
        "page_obj": page_obj,
        "total_records": len(records),
        "total_days": 22,
        "present_days": 18,
        "leave_days": 2,
        "absent_days": 1,
        "avg_hours": 9.2,
    })


def leaves(request):
    static_leaves = [
        {
            'leave_type': 'Annual Leave',
            'start_date': '2026-02-15',
            'end_date': '2026-02-15',
            'total_days': 3,
            'status': 'Approved',
            'reason': 'Family vacation'
        },
        {
            'leave_type': 'Sick Leave',
            'start_date': '2026-02-05',
            'end_date': '2026-02-05',
            'total_days': 1,
            'status': 'Approved',
            'reason': 'Medical checkup'
        },
        {
            'leave_type': 'Casual Leave',
            'start_date': '2026-02-25',
            'end_date': '2026-02-25',
            'total_days': 1,
            'status': 'Pending',
            'reason': 'Personal work'
        },
    ]

    context = {
        'all_leaves_static': static_leaves,
        'annual_remaining': 12,
        'sick_remaining': 5,
        'pending_requests': 1,
    }

    return render(request, 'leaves.html', context)


def payroll(request):
    # Standard Employee Info for the header
    employee_info = {
        'id': 'EMP-2026-084',
        'bank': 'Standard Chartered Bank',
        'account': '**** 4492',
        'pan_number': 'ABCDE1234F',
    }

    # Salary Breakdown
    earnings = [
        {'label': 'Basic Salary', 'amount': 4500.00},
        {'label': 'HRA (House Rent Allowance)', 'amount': 1200.00},
        {'label': 'Conveyance Allowance', 'amount': 300.00},
        {'label': 'Special Allowance', 'amount': 500.00},
    ]
    
    deductions = [
        {'label': 'Provident Fund (EPF)', 'amount': 180.00},
        {'label': 'Professional Tax', 'amount': 20.00},
        {'label': 'Health Insurance Premium', 'amount': 150.00},
        {'label': 'Income Tax (TDS)', 'amount': 450.00},
    ]
    
    total_earnings = sum(item['amount'] for item in earnings)
    total_deductions = sum(item['amount'] for item in deductions)
    net_salary = total_earnings - total_deductions

    # History Table
    history = [
        {'month': 'January 2026', 'total': 5850.00, 'status': 'Paid', 'date': 'Jan 31, 2026', 'id': 'PS-9920'},
        {'month': 'December 2025', 'total': 5850.00, 'status': 'Paid', 'date': 'Dec 31, 2025', 'id': 'PS-8841'},
        {'month': 'November 2025', 'total': 5700.00, 'status': 'Paid', 'date': 'Nov 30, 2025', 'id': 'PS-7712'},
    ]

    context = {
        'employee': employee_info,
        'earnings': earnings,
        'deductions': deductions,
        'total_earnings': total_earnings,
        'total_deductions': total_deductions,
        'net_salary': net_salary,
        'history': history,
        'current_month': 'February 2026'
    }
    return render(request, 'payroll.html', context)

def profile(request):
    # Data based on your current professional details
    user_data = {
        'full_name': 'Sahil Kumar', #
        'role': 'Python Django Developer', #
        'email': 'sahil.kumar@hrmpro.com',
        'phone': '+91 98765 43210',
        'location': 'Maharashtra, India', #
        'join_date': 'January 15, 2025', #
        'department': 'Engineering',
        'manager': 'Alex Thompson',
        'employment_type': 'Full-Time',
    }

    # Professional metrics
    metrics = [
        {'label': 'Projects', 'value': '4', 'icon': 'briefcase'}, # Refers to your Resume projects
        {'label': 'Attendance', 'value': '98%', 'icon': 'calendar'},
        {'label': 'Performance', 'value': '4.9', 'icon': 'star'},
    ]

    context = {
        'user': user_data,
        'metrics': metrics,
    }
    return render(request, 'profile.html', context)

def mytasks(request):
    return render(request,'mytasks.html')