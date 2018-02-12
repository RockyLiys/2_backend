# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
#from django.shortcuts import render

#from collections import OrderedDict
# Create your views here.
from django.views.generic import ListView
from misc.enum import TRAINING_DIRECTION, ALL_SKILLS, CHARACTER_TYPE
import json
import random
import time
from datetime import datetime
from adapter.models import Result
from misc.enum import power_map
from adapter.models import Hobbies, TrainingDirection
from iphone.signals import deal_result_handler


class HelloWorld(ListView):
    template_name = 'iphone/helloworld.xml'

    def get_context_data(self, **kwargs):
        context = super(HelloWorld, self).get_context_data(**kwargs)
        context['helloworld'] = "helloworld"
        return context

    def get_queryset(self):
        return []



class Index(ListView):
    template_name = 'iphone/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['helloworld'] = "helloworld"
        context["trans"] = [x[1] for x in TRAINING_DIRECTION]
        context["skills"] = [x[1] for x in ALL_SKILLS]
        context["types"] = [x[1] for x in CHARACTER_TYPE]
        return context

    def get_queryset(self):
        return []

def submit_form(request):
    if request.method == "POST":
        query_dict = request.POST
        req_json = query_dict.dict()
        req_json.pop("csrfmiddlewaretoken")
        orderId = datetime.now().strftime("%j%U%w%Y%m%d%H%M%S%s")
        obj, created = Result.objects.get_or_create(order=orderId, test_data=json.dumps(req_json))
        if not created:
            #TODO已经存一样的记录发邮件通知
            pass
        count = {
            "认知总得分": 192,
            "运动操作总得分": 23,
            "社交总得分": 34,
            "每周总花费费用": 2000,
            "每周总学习时长": 30,
            "items": {}
        }
        items={}
        for power in power_map:
            items.update({power: random.choice(range(3, 15))})
        count["items"] = items
        data = {
            "code": "0",
            "message": "Successful",
            "timestamp": int(time.time()),
            "result": "true",
            "version": "V1.0"
        }
        data["data"] = count

        return HttpResponse(json.dumps(data), content_type="application/json")

def class_ability(request):
    data = {
        "code": "0",
        "message": "Successful",
        "timestamp": int(time.time()),
        "result": "true",
        "version": "V1.0"
    }
    hobbies = Hobbies.objects.all()

    data["data"] = [{"value": h.index, "name": h.name} for h in hobbies]
    return HttpResponse(json.dumps(data), content_type="application/json")

def trainingdirection(request):
    data = {
        "code": "0",
        "message": "Successful",
        "timestamp": int(time.time()),
        "result": "true",
        "version": "V1.0"
    }
    trainingdiret = TrainingDirection.objects.all()

    data["data"] = [{"value": td.index, "name": td.name} for td in trainingdiret]
    return HttpResponse(json.dumps(data), content_type="application/json")


