# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# Create your models here.

@python_2_unicode_compatible
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=25, default="", blank=True)
    telephone = models.CharField(max_length=16, default='', blank=True, verbose_name=_(u"电话"), help_text=u"电话")
    openid = models.CharField(max_length=100, help_text=_(u"open id"))
    appkey = models.CharField(max_length=100, help_text=_(u"app key"))

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Account()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
