# -*- coding: utf-8 -*-

from celery import shared_task
from adapter.models import Result
import json

@shared_task
def analyze_result(order="345501201712110440381512967238"):
    print order
    result = Result.objects.get(order=order)
    req = json.loads(result.test_data)
    print req

