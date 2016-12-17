from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import Permission, User
from django.db import models
from django.utils import timezone


class Item(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    item_name = models.CharField(max_length=200)
    seller_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    item_cost = models.CharField(max_length=20)
    item_details = models.TextField()
    item_image = models.FileField()
    posted_date = models.DateTimeField(
            default=timezone.now)
