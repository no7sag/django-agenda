from django.db import models
from datetime import date

class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, null=True, blank=True)
    end_date = models.DateField(default=date.today)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title