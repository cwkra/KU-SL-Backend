from django.shortcuts import render
from rest_framework import viewsets, permissions
from student_loan_request_record.models import StudentLoanRequestRecord
from student_loan_request_record.serializers import (
    StudentLoanRequestRecordSerializer
)


# Create your views here.

class StudentLoanRequestRecordViewSet(viewsets.ModelViewSet):
    queryset = StudentLoanRequestRecord.objects.all()
    serializer_class = StudentLoanRequestRecordSerializer