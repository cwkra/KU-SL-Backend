from django.db import models
from authentication.models import User
from django.utils import timezone

# Create your models here.
class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, db_column='sender')
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE, db_column='receiver')
    title = models.CharField(max_length=150)
    message = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)