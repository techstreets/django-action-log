# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ActionRecord


@csrf_exempt
def get_action_records(request):

    action = request.GET.get('action', None)
    limit = int(request.GET.get('limit', 0))

    max_limit = settings.ACTION_LOG_QUERY_LIMIT
    if request.user.is_superuser:
        max_limit = settings.ACTION_LOG_ADMIN_QUERY_LIMIT

    if (limit == 0) and (max_limit == 0):
        limit = 0
    elif limit == 0:
        limit = max_limit
    elif limit > max_limit:
        limit = max_limit

    # filter out records
    records = ActionRecord.objects.all().order_by('-id')
    if action is not None:
        records = records.filter(action_type__name=action)
    if limit != 0:
        records = records.all()[:limit]

    return HttpResponse(
        json.dumps([
            record.dump(settings.ACTION_LOG_ALOWED_FIELDS)
            for record in records
        ]), content_type='application/json'
    )
