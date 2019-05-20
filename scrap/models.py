from django.db import models
from django.contrib.auth.models import User
from meeting.models import Meeting

# Create your models here.

class Scrap(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=True)
    meeting = models.ForeignKey(Meeting, related_name='scrapped', on_delete=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)