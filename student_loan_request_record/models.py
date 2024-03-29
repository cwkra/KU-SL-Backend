from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here.


class StudentLoanRequestRecord(models.Model):
    academic_year = models.CharField(max_length=10)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, db_column='borrower')
    borrower_name = models.CharField(max_length=150)
    semester = models.CharField(max_length=10)
    tuition_fees = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    create_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='รอการตรวจสอบ')