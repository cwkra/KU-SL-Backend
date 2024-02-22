from django.urls import include, path
from rest_framework.routers import DefaultRouter
from volunteer_activities_hours_record.views import (
    VolunteerActivitiesHoursRecordViewSet
)

router = DefaultRouter()
router.register(r'volunteer-activities-hours-records', VolunteerActivitiesHoursRecordViewSet, basename='volunteer-activities-hours-records')

urlpatterns = [
    path('', include(router.urls)),
]