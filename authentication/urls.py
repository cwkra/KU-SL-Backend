from django.urls import include, path
from rest_framework.routers import DefaultRouter
from authentication.views import (
    UserViewSet,
    GroupViewSet
)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
]