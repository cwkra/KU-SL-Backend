from django.urls import include, path
from rest_framework.routers import DefaultRouter
from authentication.views import (
    UserViewSet,
    EducationViewSet
)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'educations', EducationViewSet, basename='educations')

urlpatterns = [
    path('', include(router.urls)),
]