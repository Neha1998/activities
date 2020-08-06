import json

from rest_framework import serializers
from .models import User, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    activity_period = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('user_id', 'real_name', 'tz', 'activity_period')
