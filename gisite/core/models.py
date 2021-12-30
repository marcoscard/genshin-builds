from django.db import models
from django.db.models import signals

from .signals import create_slug

# Create your models here.
class Build(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    guide = models.TextField(blank=True, null=True,)
    characters = models.JSONField()
    slug = models.SlugField(max_length=170, editable=False, null=True, blank=True)
    # Field to Slug
    slug_field_name = 'slug'
    slug_from = 'title'

    def __unicode__(self):
        return self.title


signals.post_save.connect(create_slug, sender=Build)