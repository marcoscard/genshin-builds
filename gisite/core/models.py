from django.db import models

# Create your models here.
class Build(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    guide = models.TextField(blank=True, null=True)
    character_1 = models.JSONField()