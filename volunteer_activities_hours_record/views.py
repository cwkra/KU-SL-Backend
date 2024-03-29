from django.shortcuts import render
from rest_framework import viewsets, permissions
from volunteer_activities_hours_record.models import VolunteerActivitiesHoursRecord
from volunteer_activities_hours_record.serializers import (
    VolunteerActivitiesHoursRecordSerializer
)


# Create your views here.

class VolunteerActivitiesHoursRecordViewSet(viewsets.ModelViewSet):
    queryset = VolunteerActivitiesHoursRecord.objects.all().order_by('-create_date')
    serializer_class = VolunteerActivitiesHoursRecordSerializer
    
    search_fields = (
        'id',
        'borrower'
                     )
    filterset_fields = {
        'id': {'exact'},
        'borrower': {'exact'},
        'academic_year': {'exact'},
        'status': {'exact'}
    }