# -*- coding: utf-8 -*-
from django.conf.urls import url
from iphone import views
urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'helloworld/?', views.HelloWorld.as_view(), name="test"),
    url(r'submit/?', views.submit_form, name="submit"),

    url(r'classability/?', views.class_ability, name="class_abbility"),
    url(r'trainingdirection/?', views.trainingdirection, name="trainingdirection"),

]
