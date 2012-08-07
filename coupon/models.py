# coding=utf-8

from django.db import models
from shop.models import Shop

class couponProfile(models.Model):
    extra_01 = models.CharField(max_length=20)   # 额外信息01

class Coupon(models.Model):
    title = models.CharField(max_length=30)  # 优惠券的标题
    provider = models.ManyToManyField(Shop, related_name='provider') # 优惠券的提供商，与shop.Shop是多对多的关系
    accepter = models.ManyToManyField(Shop, related_name='accepter') # 接受这个优惠券的商家，与shops.Shop是多对多的关系
    profile = models.OneToOneField(couponProfile)   # 优惠券的额外信息，与couponProfile是一对一的关系

class couponHistory(models.Model):
    title = models.CharField(max_length=30)  # 优惠券操作历史的标题
    coupon = models.ForeignKey(Coupon)  # 与优惠券是多对一的关系

