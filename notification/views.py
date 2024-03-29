from django.shortcuts import render
from rest_framework import viewsets, permissions
from notification.models import Notification
from notification.serializers import (
    NotificationSerializer
)


# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-create_date')
    serializer_class = NotificationSerializer
    search_fields = (
        'id',
        'sender',
        'receiver'
                     )
    filterset_fields = {
        'sender': {'exact'},
        'id': {'exact'},
        'receiver': {'exact'},
        'message': {'contains', 'exact'},
        'is_read': {'exact'}
    }
    ordering_fields = search_fields