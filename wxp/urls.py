# -*- coding: utf-8 -*-
"""wxp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView

from wxp.schema import schema

admin.site.site_header = "WXP 后台管理"
admin.site.site_title= "WXP site"
admin.site.index_title= "WXP"
admin.site.site_url = "/iphone"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^iphone/?', include('iphone.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

