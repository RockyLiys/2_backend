# -*- coding: utf-8 -*-
import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug

from adapter.models import Category, Hobbies

# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ["index", "name"]
        interfaces = (relay.Node, )

class HobbiesNode(DjangoObjectType):
    class Meta:
        model = Hobbies
        filter_fields = {
            "index": ["exact", "icontains", "istartswith"],
            "name": ["exact", "icontains"],
        }
        interfaces = (relay.Node, )

class Query(object):
    category = relay.Node.Field(CategoryNode)
    categories = DjangoFilterConnectionField(CategoryNode)

    hobby = relay.Node.Field(HobbiesNode)
    hobbies = DjangoFilterConnectionField(HobbiesNode)

    debug = graphene.Field(DjangoDebug, name="__debug")


class CategoryQuery(ObjectType):
    my_categories = DjangoFilterConnectionField(CategoryNode)

    def resolve_my_categories(self, args, info):
        return Category.objects.all()
