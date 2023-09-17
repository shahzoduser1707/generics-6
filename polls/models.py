from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class ShopModel(models.Model):
    name = models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=200,default='')
    desc = models.TextField(default='write about shop')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = 'ShopModel'
    def __str__(self) -> str:
        return self.name