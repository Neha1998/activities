# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from user_activities.models import ActivityPeriod, User

admin.site.register(User)
admin.site.register(ActivityPeriod)