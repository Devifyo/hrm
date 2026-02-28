from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
