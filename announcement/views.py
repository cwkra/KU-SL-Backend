from django.shortcuts import render
from rest_framework import viewsets, permissions
from announcement.models import Announcement
from announcement.serializers import (
    AnnouncementSerializer
)


# Create your views here.

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all().order_by('-announced_datetime')
    serializer_class = AnnouncementSerializer
    search_fields = (
        'header',
        'description'
                     )
    filterset_fields = {
        'id': {'exact'},
        'header': {'contains', 'exact'}
    }
    ordering_fields = ('id', 'header', 'announced_datetime')