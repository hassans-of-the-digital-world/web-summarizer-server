from django.db import models


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    oauth = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

