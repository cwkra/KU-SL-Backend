
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import action

from authentication.models import User, Education
from authentication.serializers import (
    UserSerializer, 
    
    EducationSerializer,
    CreateEducationSerializer,
    UpdateEducationSerializer,
    DeleteEducationSerializer
)

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
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
    
