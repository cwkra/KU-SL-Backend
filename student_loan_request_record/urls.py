from django.urls import include, path
from rest_framework.routers import DefaultRouter
from student_loan_request_record.views import (
    StudentLoanRequestRecordViewSet
)

router = DefaultRouter()
router.register(r'student-loan-request-records', StudentLoanRequestRecordViewSet, basename='student-loan-request-records')

urlpatterns = [
    path('', include(router.urls)),
]