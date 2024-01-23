import graphene
import uuid
from models import Link, User
from objects import LinkObject, UserObject
from modules import db


class AddUpvote(graphene.Mutation):
    class Arguments:
        link_id = graphene.String(required=True)
    link = graphene.Field(lambda: LinkObject)

    def mutate(self, info, link_id):
        link = Link.query.filter_by(link_id=link_id).first()
        link.upvotes += 1
        return AddUpvote(link=link)

  
class CreateLink(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        url = graphene.String(required=True) 
        user_id = graphene.String(required=False)
        upvotes = graphene.Int(required=False)
    link = graphene.Field(lambda: LinkObject)

    def mutate(self, info, title, url, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        link = Link(link_id=str(uuid.uuid4()), title=title, url=url, upvotes=1)
        if user is not None:
            link.creator = user
        db.session.add(link)
        db.session.commit()
        return CreateLink(link=link)
    
class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=False) 
    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username, email):
        user = User(user_id=str(uuid.uuid4()), username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_user = CreateUser.Field()
    add_upvote = AddUpvote.Field()