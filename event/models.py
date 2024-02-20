from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=150)
    location_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)