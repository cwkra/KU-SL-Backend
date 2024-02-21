from django.shortcuts import render
from rest_framework import viewsets, permissions
from qualification_question.models import QualificationQuestion
from qualification_question.serializers import (
    QualificationQuestionSerializer
)


# Create your views here.

class QualificationQuestionViewSet(viewsets.ModelViewSet):
    queryset = QualificationQuestion.objects.all()
    serializer_class = QualificationQuestionSerializer