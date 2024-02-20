from django.shortcuts import render
from rest_framework import viewsets, permissions
from event.models import Event
from event.serializers import (
    EventSerializer
)


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer