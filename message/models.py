from django.db import models
from django.contrib.auth.models import User
from meeting.models import Meeting

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=True)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=True)
    meeting = models.ForeignKey(Meeting, related_name='meeting', on_delete=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    def summary(self):
        return self.content[:20]