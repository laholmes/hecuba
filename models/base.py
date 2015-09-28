# base model pattern - subclasses will automatically use the correct storage
# http://charlesleifer.com/docs/peewee/peewee/models.html#model-api-smells-like-django
from peewee import *

database = SqliteDatabase('hecuba.db')

class Base(Model):
    class Meta:
        database = database
