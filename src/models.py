from sqlalchemy.orm import backref
from config import db as database

class Subscription(database.Model):
    __tablename__ = 'subscriptions'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.String, nullable=False)
    price = database.Column(database.Integer, nullable=False)
    users = database.relationship('User', backref='subscription')
    
    def __repr__(self):
        return '<Subscription %r>' % self.title
    

class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True),
    username = database.Column(database.String, unique=True, nullable=False)
    email = database.Column(database.String, unique=True, nullable=False)
    password = database.Column(database.String, nullable=False)
    subscription_id = database.Column(database.Integer, database.ForeignKey('subscriptions.id'))
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    