from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=200, default='first_name')
    middle_name = models.CharField(max_length=200, default='second_name')
    last_name = models.CharField(max_length=200, default='last_name')
    nick_name = models.CharField(max_length=200, default='nick_name')
