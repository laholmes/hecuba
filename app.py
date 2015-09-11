import datetime
from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from functools import wraps
from hashlib import md5
from peewee import *

DATABASE = 'hecuba.db'
DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'

app = Flask(__name__)
app.config.from_object(__name__)

database = SqliteDatabase(DATABASE)

# base model pattern - subclasses will automatically use the correct storage
# http://charlesleifer.com/docs/peewee/peewee/models.html#model-api-smells-like-django
class BaseModel(Model):
    class Meta:
        database = database

# the user model specifies its fields (or columns) declaratively, like django
# class User(BaseModel):
    # username = CharField(unique=True)
    # password = CharField()
    # email = CharField()
    # join_date = DateTimeField()

    # class Meta:
    #     order_by = ('username',)

    # # it often makes sense to put convenience methods on model instances, for
    # # example, "give me all the users this user is following":
    # def following(self):
    #     # query other users through the "relationship" table
    #     return User.select().join(
    #         Relationship, on=Relationship.to_user,
    #     ).where(Relationship.from_user == self)

    # def followers(self):
    #     return User.select().join(
    #         Relationship, on=Relationship.from_user,
    #     ).where(Relationship.to_user == self)

    # def is_following(self, user):
    #     return Relationship.select().where(
    #         (Relationship.from_user == self) &
    #         (Relationship.to_user == user)
    #     ).count() > 0

    # def gravatar_url(self, size=80):
    #     return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
    #         (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)

class Team(BaseModel):
    name = CharField()

class Player(BaseModel):
    first_name = CharField()
    last_name = CharField()
    dob = DateField()
    team_id = ForeignKeyField(Team, related_name='team')

# simple utility function to create tables
def create_tables():
    database.connect()
    database.create_tables([User, Relationship, Message])

# given a template and a SelectQuery instance, render a paginated list of
# objects from the query inside the template
def object_list(template_name, qr, var_name='object_list', **kwargs):
    kwargs.update(
        page=int(request.args.get('page', 1)),
        pages=qr.count() / 20 + 1
    )
    kwargs[var_name] = qr.paginate(kwargs['page'])
    return render_template(template_name, **kwargs)

# retrieve a single object matching the specified query or 404 -- this uses the
# shortcut "get" method on model, which retrieves a single object or raises a
# DoesNotExist exception if no matching object exists
# http://charlesleifer.com/docs/peewee/peewee/models.html#Model.get)
def get_object_or_404(model, *expressions):
    try:
        return model.get(*expressions)
    except model.DoesNotExist:
        abort(404)

# Request handlers -- these two hooks are provided by flask and we will use them
# to create and tear down a database connection on each request.
@app.before_request
def before_request():
    g.db = database
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def homepage():
    teams = Teams.select()
    return object_list('teams.html', teams, 'team_list')

@app.route('/teams/')
def public_timeline():
    teams = Teams.select()
    return object_list('teams.html', teams, 'team_list')

# allow running from the command line
if __name__ == '__main__':
    app.run()