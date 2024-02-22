from django.db import models
from authentication.models import User

# Create your models here.


class VolunteerActivitiesHoursRecord(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    hours = models.IntegerField()
    location_name = models.CharField(max_length=10)
    academic_year = models.CharField(max_length=10)
    create_date = models.DateTimeField()
    verification = models.FileField(upload_to='private/verify/')
    status = models.CharField(max_length=20, default='รอการยืนยัน')