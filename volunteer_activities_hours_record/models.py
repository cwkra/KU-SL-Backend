from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here.


class VolunteerActivitiesHoursRecord(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, db_column='borrower')
    borrower_name = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    hours = models.IntegerField()
    location_name = models.CharField(max_length=150)
    academic_year = models.CharField(max_length=10)
    create_date = models.DateTimeField(default=timezone.now)
    verification = models.FileField(upload_to='verify/')
    event_date = models.DateField()
    status = models.CharField(max_length=20, default='รอการยืนยัน')