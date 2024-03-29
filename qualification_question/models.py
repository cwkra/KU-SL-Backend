from django.db import models

# Create your models here.

QUESTION_TYPE = [
    ('MultipleChoice', 'Multiple Choice'),
    ('Checkbox', 'Checkbox')
]

class QualificationQuestion(models.Model):
    question = models.CharField(max_length=150)
    choice = models.JSONField()
    correct_answer = models.JSONField()