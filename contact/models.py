from django.db import models
from datetime import date

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_num1 = models.CharField(max_length=15)
    phone_num2 = models.CharField(max_length=15, null=True, blank=True)
    company = models.CharField(max_length=30)
    join_date = models.DateField(default=date.today)
    notes = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'