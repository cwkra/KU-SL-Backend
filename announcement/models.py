from django.db import models
from django.utils import timezone

# Create your models here.
class Announcement(models.Model):
    header = models.CharField(max_length=150)
    announced_datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)