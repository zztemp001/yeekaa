# Create your models here.
# coding=utf-8

from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

class shopHistory(models.Model):
    title = models.CharField(max_length=30)
    shop = models.ForeignKey(Shop)
