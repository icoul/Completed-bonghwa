from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

# Create your models here.
class Contents(models.Model):
    mentionIndex  = models.CharField(max_length=5, default='0')  # 멘션 index
    mentionDepth  = models.CharField(max_length=5, default='0')  # 멘션 순서
    username      = models.CharField(max_length=40)              # 유저 아이디
    contents      = models.CharField(max_length=150)             # 장작 내용
    image         = models.FileField(null=True)                  # 그림
    createdDate   = models.DateTimeField(auto_now=True)          # 작성일
    dm            = models.IntegerField(default=0)               # DM여부
    deleted       = models.IntegerField(default=0)               # 삭제여부

    def __str__(self):
        return self.contents
