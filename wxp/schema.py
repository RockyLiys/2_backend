# -*- coding: utf-8 -*-
import graphene
from iphone import schema as iphone_schema
from adapter import schema as adapter_schema

class Query(iphone_schema.Query, graphene.ObjectType):
    pass

class QueryId(iphone_schema.QueryId, graphene.ObjectType):
    pass

class QueryHello(iphone_schema.QueryHello, graphene.ObjectType):
    pass


class AdapterQuery(adapter_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
schema = graphene.Schema(query=AdapterQuery)

