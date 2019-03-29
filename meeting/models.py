from django.db import models

# Create your models here.
class Meeting(models.Model):
    category = models.CharField(max_length=20)
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