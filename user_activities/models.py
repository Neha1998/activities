# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ActivityPeriod(models.Model):
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    def as_dict(self):
        context = {
            'start_time': self.start_time,
            'end_time': self.end_time
        }

        return context


class User(models.Model):
    real_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)
    activity_period = models.ManyToManyField(ActivityPeriod)

    def __str__(self):
        return self.real_name
