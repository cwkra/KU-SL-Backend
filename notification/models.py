from django.db import models
from authentication.models import User

# Create your models here.
class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.TextField()
    create_date = models.DateTimeField()
    is_read = models.BooleanField(default=False)