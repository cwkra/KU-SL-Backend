from django.shortcuts import render
from rest_framework import viewsets, permissions
from notification.models import Notification
from notification.serializers import (
    NotificationSerializer
)


# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer