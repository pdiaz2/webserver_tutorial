from datetime import datetime
from flaskblog import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager
from flask_login import UserMixin
from flask import current_app
# Beware of circular imports!!!

# each of this classes is like a "row" in the table
# everytime I create a user in terminal its user = User()
# duh -> Object Relational Mapper: row <=> instance of class
# then there is a constructor to integrate them (the "commit")
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    # check this out !!! backreference
    # - the backreference would be the "name" for the relationship link
    # - I am saying that the field 'posts' is related to the class Post
    # - and that I can call it through the 'alias' author (which is NOT)
    # - a column in the User model. Then SQLAlchemy links that through
    # - the ForeignKey 'user.id0 called in Post model and I can get
    # - THE OBJECT id is user.id (i need to diagram this)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # The utcnow will be called when commiting to the database, not when creating the object
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # Foreign key points to a key in another DB. Which you ask?
    # - To the user TABLE (lowercase) (not Class!!!!). Notice that in the User
    # - class the reference is to the Post CLASS (Uppercase)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"