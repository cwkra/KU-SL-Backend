from django.db import models

# Create your models here.
class Announcement(models.Model):
    header = models.CharField(max_length=150)
    announced_datetime = models.DateTimeField()
    description = models.TextField(null=True, blank=True)