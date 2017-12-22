# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 03:19

from django.db import migrations
from misc.enum import CATEGORY, ALL_SKILLS, ABILITY

app_label = "adapter"

def forwards_func(apps, schema_editor):
    Category = apps.get_model(app_label, "Category")
    db_alias = schema_editor.connection.alias
    category_dict = []
    for t in CATEGORY:
        category_dict.append(Category(index=t[0], name=t[1]))
    Category.objects.using(db_alias).bulk_create(category_dict)
    Hobbies = apps.get_model(app_label, "Hobbies")
    hobbies_dict = []
    for t in ALL_SKILLS:
        hobbies_dict.append(Hobbies(index=t[0], name=t[1]))
    Hobbies.objects.using(db_alias).bulk_create(hobbies_dict)
    Power = apps.get_model(app_label, "Power")
    powers = []
    for p in ABILITY:
        powers.append(Power(index=p[0], name=p[1]))
    Power.objects.using(db_alias).bulk_create(powers)


def reverse_func(apps, schema_editor):
    Category = apps.get_model(app_label, "Category")
    db_alias = schema_editor.connection.alias
    for t in CATEGORY:
        Category.objects.using(db_alias).filter(category_id=t[0]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('adapter', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

