import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from models import Link, User

class LinkObject(SQLAlchemyObjectType):
    class Meta:
        model = Link
        interfaces = (graphene.relay.Node, )

class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )