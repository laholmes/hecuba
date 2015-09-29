# base model pattern
# http://charlesleifer.com/docs/peewee/peewee/models.html#model-api-smells-like-django
from peewee import *

database = SqliteDatabase('hecuba.db')

class Base(Model):
    class Meta:
        database = database
