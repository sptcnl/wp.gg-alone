from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True) 
    email = models.EmailField(unique=True)
    riot_username = models.CharField(max_length=15, null=True, blank=True)  # 리그 오브 레전드 유저명
    riot_tag = models.CharField(max_length=15, null=True, blank=True)  # 리그 오브 레전드 서버명
    
    def __str__(self):
        return self.username