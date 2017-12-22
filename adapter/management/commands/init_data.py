# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from adapter.models import Category, Power, Hobbies, Ability, AbilityWeight, TrainingDirection
from django.conf import settings
from misc.enum import TRAINING_DIRECTION
import json
import os

FILE_DIR = os.path.join(settings.BASE_DIR, "conf")
def get_file_data(filename):
    file_path = os.path.join(FILE_DIR, filename)
    print file_path
    data = ""
    with open(file_path, "r") as f:
        data = f.read()
    return json.loads(data)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Activate a fixed locale, e.g. Russi
        translation.activate('ru')
        # Or you can activate the LANGUAGE_CODE # chosen in the settings:
        from django.conf import settings
        translation.activate(settings.LANGUAGE_CODE)
        # Your command logic here
        power_data = get_file_data("power.json")
        power_weight_data = get_file_data("power_weight.json")

        powers = []
        for p in power_data:
            ability = Ability(
                category_id=Category.objects.filter(name=p[u"分类"]).get(),
                hobby_id=Hobbies.objects.filter(name=p[u"名称"]).get(),
                zhou_min_speed=p[u"周最少花费最少(*100"],
                zhou_min_hours=p[u"周时间占用小时"],
                fit_age=p[u"最早适宜年龄"],
                #zonghefenxi=p[],
                luojituili=p[u"逻辑推理能力"],
                chouxiangsiwei=p[u"抽象思维能力"],
                kongjianxiangxiang=p[u"空间想象能力"],
                dulisikao=p[u"独立思考能力"],
                dajv_zhengti=p[u"大局观/整体观"],
                zhuanzhu=p[u"专注能力"],
                jisuan=p[u"计算能力"],
                xizhiguancha=p[u"细致观察能力"],
                xiangxiang=p[u"想象能力"],
                jiyi=p[u"记忆能力"],
                shenmei=p[u"审美能力"],
                shouyanxietiao=p[u"手眼协调能力"],
                secaidapei=p[u"色彩搭配能力"],
                biaoyan=p[u"表演能力"],
                jiejuewenti=p[u"解决问题能力"],
                xingtikongzhi=p[u"形体控制能力"],
                shentirouren=p[u"身体柔韧能力"],
                zhitixietiao=p[u"肢体协调能力"],
                chuangxin=p[u"创新能力"],
                yuedu=p[u"阅读能力"],
                shuxie=p[u"书写能力"],
                yuyanbiaoda=p[u"语言表达能力"],
                renjijiaowang=p[u"人际交往能力"],
                tuanduixiezuo=p[u"团队协作能力"],
                zuzhi=p[u"组织能力"],
                lingdao=p[u"领导能力"],
                kangya=p[u"抗挫折/坚韧能力"]
            )
            powers.append(ability)
        Ability.objects.bulk_create(powers)

        power_weights = []
        for p in power_weight_data:
            p_weight = AbilityWeight(
                category_id=Category.objects.filter(name=p[u"类型"]).get(),
                power_id=Power.objects.filter(name=p[u"能力名称"]).get(),
                within=p[u"内向"],
                extrovert=p[u"外向"],
                no_sure=p[u"不确定"],
                boy=p[u"男"],
                girl=p[u"女"],
                one=p[u"一类"],
                two=p[u"二类"],
                three=p[u"三类"]
            )
            power_weights.append(p_weight)
        AbilityWeight.objects.bulk_create(power_weights)

        # 培养方向
        trainings = []
        for td in TRAINING_DIRECTION:
            training_direction = TrainingDirection(
                index=td[0],
                name=td[1],
                renzhi=td[2],
                caozuo=td[3],
                shejiao=td[4],
                total=td[5]
            )
            trainings.append(training_direction)
        TrainingDirection.objects.bulk_create(trainings)

        translation.deactivate()
