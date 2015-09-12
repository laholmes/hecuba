from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from functools import wraps
from hashlib import md5
from peewee import *
from models.Team import Team

DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'
DATABASE = 'hecuba.db'
database = SqliteDatabase(DATABASE)

app = Flask(__name__)
app.config.from_object(__name__)

def object_list(template_name, qr, var_name='object_list', **kwargs):
    kwargs.update(
        page=int(request.args.get('page', 1)),
        pages=qr.count() / 20 + 1)

    kwargs[var_name] = qr.paginate(kwargs['page'])
    return render_template(template_name, **kwargs)

def get_object_or_404(model, *expressions):
    try:
        return model.get(*expressions)
    except model.DoesNotExist:
        abort(404)

# Request handlers - these two hooks are provided by flask and are used
# to create and tear down a database connection on each request.
@app.before_request
def before_request():
    g.db = database
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

# run from cmd
if __name__ == '__main__':
    app.run()
