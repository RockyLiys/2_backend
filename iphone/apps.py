# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class IphoneConfig(AppConfig):
    name = 'iphone'

    def ready(self):
        from  iphone.signals import deal_result_handler



