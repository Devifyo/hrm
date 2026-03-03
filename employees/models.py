from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#employee profile for adding details for the employee 


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_id = models.CharField(unique = True, max_length = 50)
    phone = models.CharField( max_length = 20, blank=True)
    department = models.CharField(max_length = 40)
    designation = models.CharField(max_length = 40)

    join_date = models.DateField(blank = True, null=True)

    manager = models.ForeignKey(
        User,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'team_members'
    )

    def __str__(self):
        return f"{self.user.username} Profile"
    

#attendance model for employee  
    
class Attendance(models.Model):
    employee = models.ForeignKey(
        EmployeeProfile,
        on_delete=models.CASCADE,
        related_name="attendances"
    )

    date = models.DateField(default=timezone.localdate)

    clock_in = models.DateTimeField(null=True, blank=True)
    clock_out = models.DateTimeField(null=True, blank=True)

    working_hours = models.DurationField(null=True, blank=True)

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"
