from pony import orm
from config import db_params


db = orm.Database(**db_params)


class Student(db.Entity):
    full_name = orm.Required(str)
    age = orm.Required(int)
