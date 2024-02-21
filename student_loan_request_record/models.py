from django.db import models
from authentication.models import User

# Create your models here.


class StudentLoanRequestRecord(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)
    tuition_fees = models.IntegerField()
    create_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='รอการตรวจสอบ')