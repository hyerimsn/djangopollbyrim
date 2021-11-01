from django.db import models

# Create your models here.
class User(models.Model):
    answer=models.CharField(default='', max_length=30, null=True, blank=True)
    score=models.IntegerField(default=0, blank=True)