from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ParaHuman(models.Model):

    cape_name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "ParaHuman"
        verbose_name_plural = "ParaHumans"

    def __unicode__(self):
        return self.cape_name


class Entrance(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    parahumans = models.ManyToManyField(ParaHuman, related_name='entrances')
