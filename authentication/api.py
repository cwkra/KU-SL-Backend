from django.conf import settings
from django.http import JsonResponse
from authentication.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'username': request.user.username,
        'email': request.user.email,
    })