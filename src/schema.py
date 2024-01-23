import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from mutations import Mutation
from objects import LinkObject, UserObject


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_links = SQLAlchemyConnectionField(LinkObject)
    all_users = SQLAlchemyConnectionField(UserObject)

schema = graphene.Schema(query=Query, mutation=Mutation)
