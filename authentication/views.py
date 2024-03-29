
from rest_framework import viewsets, permissions
from authentication.models import User, Education
from authentication.serializers import (
    UserSerializer, 
    EducationSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    search_fields = (
        'username',
        'id'
                     )
    filterset_fields = {
        'username': {'exact'},
        'id': {'exact'},
    }
    ordering_fields = search_fields
    permission_classes = [permissions.IsAuthenticated]

       
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    search_fields = (
        'student_id_number',
        'faculty',
        'department',
        'education_level',
        'status'
                     )
    filterset_fields = {
        'name': {'contains', 'exact'},
        'active': {'exact'},
        'student_id_number': {'exact'},
        'faculty': {'contains', 'exact'},
        'department': {'contains', 'exact'},
        'education_level': {'contains', 'exact'},
        'status': {'contains', 'exact'}
    }
    ordering_fields = search_fields
    