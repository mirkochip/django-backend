from django.db import models


class DeveloperInfo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
