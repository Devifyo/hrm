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
