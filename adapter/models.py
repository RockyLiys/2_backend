# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.models import User
# Create your models here.


class BasicModel(models.Model):
    start_time = models.DateTimeField(max_length=20, editable=False, blank=True, auto_now_add=True, verbose_name=_(u"开始时间"))
    update_time = models.DateTimeField(max_length=20, editable=False, blank=True, auto_now=True, verbose_name=_(u"更新时间"))

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Category(BasicModel):
    index = models.SmallIntegerField(verbose_name=_(u"索引"))
    name = models.CharField(max_length=50,verbose_name=_(u"分类"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u"分类")
        verbose_name_plural = _(u"分类")

@python_2_unicode_compatible
class Hobbies(BasicModel):
    #category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    index = models.SmallIntegerField(verbose_name=_(u"索引"))
    name = models.CharField(max_length=50,verbose_name=_(u"兴趣"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u"兴趣")
        verbose_name_plural = _(u"兴趣")

@python_2_unicode_compatible
class Ability(BasicModel):
    uid = models.CharField(max_length=32, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_(u"分类"))
    hobby_id = models.ForeignKey(Hobbies, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_(u"兴趣"))
    zhou_min_speed = models.PositiveSmallIntegerField(verbose_name=_(u"周最少花费最少(*100"), default=0)
    zhou_min_hours = models.PositiveSmallIntegerField(verbose_name=_(u"周时间占用小时"), default=0)
    fit_age = models.PositiveSmallIntegerField(verbose_name=_(u"最早适宜年龄"), default=0)
    zonghefenxi = models.PositiveSmallIntegerField(verbose_name=_(u"综合分析能力"), default=0)
    luojituili = models.PositiveSmallIntegerField(verbose_name=_(u"逻辑推理能力"), default=0)
    chouxiangsiwei = models.PositiveSmallIntegerField(verbose_name=_(u"抽象思维能力"), default=0)
    kongjianxiangxiang = models.PositiveSmallIntegerField(verbose_name=_(u"空间想象能力"), default=0)
    dulisikao = models.PositiveSmallIntegerField(verbose_name=_(u"独立思考能力"), default=0)
    dajv_zhengti = models.PositiveSmallIntegerField(verbose_name=_(u"大局观/整体观"), default=0)
    zhuanzhu = models.PositiveSmallIntegerField(verbose_name=_(u"专注能力"), default=0)
    jisuan = models.PositiveSmallIntegerField(verbose_name=_(u"计算能力"), default=0)
    xizhiguancha = models.PositiveSmallIntegerField(verbose_name=_(u"细致观察能力"), default=0)
    xiangxiang = models.PositiveSmallIntegerField(verbose_name=_(u"想象能力"), default=0)
    jiyi = models.PositiveSmallIntegerField(verbose_name=_(u"记忆能力"), default=0)
    shenmei = models.PositiveSmallIntegerField(verbose_name=_(u"审美能力"), default=0)
    shouyanxietiao = models.PositiveSmallIntegerField(verbose_name=_(u"手眼协调能力"), default=0)
    secaidapei = models.PositiveSmallIntegerField(verbose_name=_(u"色彩搭配能力"), default=0)
    biaoyan = models.PositiveSmallIntegerField(verbose_name=_(u"表演能力"), default=0)
    jiejuewenti = models.PositiveSmallIntegerField(verbose_name=_(u"解决问题能力"), default=0)
    xingtikongzhi = models.PositiveSmallIntegerField(verbose_name=_(u"形体控制能力"), default=0)
    shentirouren = models.PositiveSmallIntegerField(verbose_name=_(u"身体柔韧能力"), default=0)
    zhitixietiao = models.PositiveSmallIntegerField(verbose_name=_(u"肢体协调能力"), default=0)
    chuangxin = models.PositiveSmallIntegerField(verbose_name=_(u"创新能力"), default=0)
    yuedu = models.PositiveSmallIntegerField(verbose_name=_(u"阅读能力"), default=0)
    shuxie = models.PositiveSmallIntegerField(verbose_name=_(u"书写能力"), default=0)
    yuyanbiaoda = models.PositiveSmallIntegerField(verbose_name=_(u"语言表达能力"), default=0)
    renjijiaowang = models.PositiveSmallIntegerField(verbose_name=_(u"人际交往能力"), default=0)
    tuanduixiezuo = models.PositiveSmallIntegerField(verbose_name=_(u"团队协作能力"), default=0)
    zuzhi = models.PositiveSmallIntegerField(verbose_name=_(u"组织能力"), default=0)
    lingdao = models.PositiveSmallIntegerField(verbose_name=_(u"领导能力"), default=0)
    kangya = models.PositiveSmallIntegerField(verbose_name=_(u"抗挫折/坚韧能力"), default=0)

    def __str__(self):
        return self.uid


    class Meta:
        verbose_name = _(u"数值表")
        verbose_name_plural = _(u"数值表")

@python_2_unicode_compatible
class Power(BasicModel):
    index = models.SmallIntegerField(verbose_name=_(u"索引"))
    name = models.CharField(verbose_name=_(u"名称"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u"能力")
        verbose_name_plural = _(u"能力")

@python_2_unicode_compatible
class TrainingDirection(BasicModel):
    index = models.SmallIntegerField(verbose_name=_(u"索引"))
    name = models.CharField(verbose_name=_(u"培养方向"), max_length=50)
    renzhi = models.IntegerField(verbose_name=_(u"认知"))
    caozuo = models.IntegerField(verbose_name=_(u"操作"))
    shejiao = models.IntegerField(verbose_name=_(u"社交"))
    total = models.IntegerField(verbose_name=_(u"总分"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u"培养方向")
        verbose_name_plural = _(u"培养方向")



#@python_2_unicode_compatible
class AbilityWeight(BasicModel):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_(u"类型"))
    power_id = models.ForeignKey(Power, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_(u"能力"))
    within = models.DecimalField(verbose_name=_(u"内向"), max_digits=2, decimal_places=1, blank=True)
    extrovert = models.DecimalField(verbose_name=_(u"外向"), max_digits=2, decimal_places=1, blank=True)
    no_sure = models.DecimalField(verbose_name=_(u"不确定"), max_digits=2, decimal_places=1, blank=True)
    boy = models.DecimalField(verbose_name=_(u"男"), max_digits=2, decimal_places=1, blank=True)
    girl = models.DecimalField(verbose_name=_(u"女"), max_digits=2, decimal_places=1, blank=True)
    one = models.DecimalField(verbose_name=_(u"一类"), max_digits=2, decimal_places=1, blank=True)
    two = models.DecimalField(verbose_name=_(u"二类"), max_digits=2, decimal_places=1, blank=True)
    three = models.DecimalField(verbose_name=_(u"三类"), max_digits=2, decimal_places=1, blank=True)


    class Meta:
        verbose_name = _(u"能力权重")
        verbose_name_plural = _(u"能力权重")



@python_2_unicode_compatible
class Result(BasicModel):
    order = models.CharField(max_length=32, verbose_name=_(u"单号"), blank=False, null=False)
    test_data = models.TextField(max_length=1024, verbose_name=_(u"测试数据"))
    test_result = models.TextField(max_length=1024, verbose_name=_(u"测试结果"))

    def __str__(self):
        return u"{}".format(self.order)

    class Meta:
        verbose_name = (u"测试记录")
        verbose_name_plural = (u"测试记录")
