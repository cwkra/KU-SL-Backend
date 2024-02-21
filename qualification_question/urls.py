from django.urls import include, path
from rest_framework.routers import DefaultRouter
from qualification_question.views import (
    QualificationQuestionViewSet
)

router = DefaultRouter()
router.register(r'qualification-questions', QualificationQuestionViewSet, basename='qualification-questions')

urlpatterns = [
    path('', include(router.urls)),
]