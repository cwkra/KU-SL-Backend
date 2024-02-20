from django.urls import include, path
from rest_framework.routers import DefaultRouter
from event.views import (
    EventViewSet
)

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]