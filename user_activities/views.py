# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import User


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {"ok": True, "members": []}

        for user in users:  # populate list
            context['members'].append({
                'id': user.user_id,
                'real_name': user.real_name,
                'tz': user.tz,
                'activity_periods': [x.as_dict() for x in user.activity_period.all()]
            })

        json_context = json.dumps(context, cls=DjangoJSONEncoder)  # dump list as JSON
        return HttpResponse(json_context, 'application/javascript')
