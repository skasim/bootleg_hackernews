from modules import db
import uuid


# Models: Defines the SQLAlchemy objects
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(120), primary_key=True, index=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    links = db.relationship('Link', backref='creator')

    def __init__(self, user_id, username, email):
      self.user_id = user_id
      self.username = username
      self.email = email

    def __repr__(self):
        return '<User %r>' % self.user_id


class Link(db.Model):
    __tablename__ = 'links'

    link_id = db.Column(db.String(120), primary_key=True)
    title = db.Column(db.String(256), index=True, nullable=False)
    url = db.Column(db.Text, nullable=False)
    upvotes = db.Column(db.Integer)
    user_id = db.Column(db.String, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f"<Link {self.title} {self.url} {self.upvotes} {self.user_id}>"
