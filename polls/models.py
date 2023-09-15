from django.db import models
from datetime import datetime
# Create your models here.


class ShopModel(models.Model):
    name = models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=200,default='')
    desc = models.TextField(default='write about shop')

    class Meta:
        db_table = 'ShopModel'
    def __str__(self) -> str:
        return self.name