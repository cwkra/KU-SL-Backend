from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import (
    UserViewSet,
    EducationViewSet,
)
from . import api
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'educations', EducationViewSet, basename='educations')


urlpatterns = [
    path('', include(router.urls)),
    path('me/', api.me, name='me'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
