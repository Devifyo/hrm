from django.db import models

# Create your models here.

class DailyQuote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length = 30)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"Quote for {self.date}"

