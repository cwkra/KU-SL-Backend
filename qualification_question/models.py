from django.db import models

# Create your models here.

QUESTION_TYPE = [
    ('MultipleChoice', 'Multiple Choice'),
    ('Checkbox', 'Checkbox')
]

class QualificationQuestion(models.Model):
    question = models.CharField(max_length=150)
    choice = models.JSONField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE)