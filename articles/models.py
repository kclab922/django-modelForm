from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    # add(추가)가 되었을 때의 시간을 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 추가와 관계없이 현재시간을 저장 
    updated_at = models.DateTimeField(auto_now=True)
