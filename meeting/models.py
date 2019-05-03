from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    user = models.ForeignKey(User, related_name='meetings', on_delete=models.CASCADE)
    CATEGORIES = [('식사', '식사'), ('문화', '문화'), ('스포츠/레저', '스포츠/레저'), ('취미/힐링', '취미/힐링'), ('스터디', '스터디'), ('기타', '기타')]
    category = models.CharField(max_length=10, choices=CATEGORIES)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    date = models.DateField() # 날짜 지정
    start_time = models.TimeField() # 시작 시각
    end_time = models.TimeField() # 끝나는 시각
    created_at = models.DateTimeField(auto_now_add=True) # 만든 시각 자동 저장
    updated_at = models.DateTimeField(auto_now=True) # 수정 시각 자동 저장

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]