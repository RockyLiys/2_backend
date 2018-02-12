# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
from adapter.models import Result
# signal  同步的，如果用并行，还是要用celery

@receiver(post_save, sender=Result)
def deal_result_handler(sender, **kwargs):
    obj = kwargs['instance']
    json.loads(obj.test_data)
    sender.objects.filter(order=obj.order).update(test_result="TODO 计算结果")


