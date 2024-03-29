from django.shortcuts import render
from rest_framework import viewsets, permissions
from student_loan_request_record.models import StudentLoanRequestRecord
from student_loan_request_record.serializers import (
    StudentLoanRequestRecordSerializer
)


# Create your views here.

class StudentLoanRequestRecordViewSet(viewsets.ModelViewSet):
    queryset = StudentLoanRequestRecord.objects.all().order_by('-create_date')
    serializer_class = StudentLoanRequestRecordSerializer
    search_fields = (
        'id',
        'borrower',
        'semester',
        'academic_year',
        'status'
                     )
    filterset_fields = {
        'id': {'exact'},
        'borrower': {'exact'},
        'semester': {'exact'},
        'academic_year': {'exact'},
        'status' : {'exact'}
    }