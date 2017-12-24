# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from adapter.account.models import Account
from django.utils.translation import ugettext_lazy as _

# Register your models here.
# Define an inline admin descriptor for Account model
# which acts a bit like a singleton
class AccountInline(admin.StackedInline):
    model = Account
    max_num = 1
    can_delete = False
    verbose_name_plural = _(u"附加信息")

# Define a new User admin
class UserAccountAdmin(BaseUserAdmin):
    inlines = (AccountInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAccountAdmin)
