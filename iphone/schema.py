# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User as UserModel

from graphene_django import DjangoObjectType
import graphene

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        #interfaces = (graphene.Node,)
        #filter_fields = [
        #    "id",
        #    "username",
        #]

class Query(object):
    users = graphene.List(User)

    @graphene.resolve_only_args
    def resolve_users(self):
        return UserModel.objects.all()


class QueryId(object):
    user = graphene.Field(User,id=graphene.Int()) #指定id字段作为查询参数
    users = graphene.List(User)

    #@graphene.resolve_only_args #注释装饰器，接收args参数
    def resolve_users(self, info,**kwargs):
        return UserModel.objects.all()

    def resolve_user(self, info, **kwargs):
        print info, kwargs
        id = kwargs.get('id', None)
        if id is not None:
            return UserModel.objects.filter(pk=id).get() #否则返回过滤后的结果


"""
class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)

    def mutate(self, args, content, info):
        user = User(username=args.get('username'))
        ok = True
        return CreateUser(ok=ok, user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
"""
#schema = graphene.Schema(query=Query, mutation=Mutation)

class QueryHello(object):  # 2

    hello = graphene.String(description='A typical world')  # 3
    world = graphene.String(description='A typical hello')  # 3

    def resolve_hello(self, info, **kwargs):  # 4
        return 'World'

    def resolve_world(self, info, **kwargs):  # 4
        return 'Hello'

