# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,  Hobbies, Power, Ability, AbilityWeight, TrainingDirection, Result
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ("index", "name")
    list_display = fields


@admin.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ("index", "name")
    list_display = fields


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ("index", "name")
    list_display = fields

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ("uid","category_id", "hobby_id", "zhou_min_speed", "zhou_min_hours", "fit_age", "zonghefenxi", \
        "luojituili", "chouxiangsiwei", "kongjianxiangxiang", "dulisikao", "dajv_zhengti", "zhuanzhu", "jisuan", \
        "xizhiguancha", "xiangxiang", "jiyi", "shenmei", "shouyanxietiao", "secaidapei", "secaidapei", \
        "biaoyan", "jiejuewenti", "xingtikongzhi", "shentirouren", "zhitixietiao", "chuangxin", \
        "yuedu", "shuxie", "yuyanbiaoda", "renjijiaowang", "tuanduixiezuo", "zuzhi", "lingdao", "kangya"
    )
    """
    fieldsets = (
        (u"",{
            "fields": ()
        })
    )
    """



@admin.register(AbilityWeight)
class AbilityWeightAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ("category_id", "power_id", "within", "extrovert", "no_sure", "boy", "girl", "one", "two", "three")


@admin.register(TrainingDirection)
class TrainingDirectionAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ("index", "name", "renzhi", "caozuo", "shejiao", "total")


def _test_data(obj):
    return (u"查看测试内容",)
def _test_result(obj):
    return (u"查看测试结果",)
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    #list_display = ("order", _test_data, _test_result)
    list_display = ("order", "test_data", "test_result")
