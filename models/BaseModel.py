# base model pattern - subclasses will automatically use the correct storage
# http://charlesleifer.com/docs/peewee/peewee/models.html#model-api-smells-like-django
from peewee import *

DATABASE = 'hecuba.db'
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database
