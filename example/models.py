from pony import orm
from config import db_params


db = orm.Database(**db_params)


class Student(db.Entity):
    full_name = orm.Required(str)
    age = orm.Required(int)
    group = orm.Required("Group")


class Group(db.Entity):
    name = orm.Required(str)
    students = orm.Set(Student)